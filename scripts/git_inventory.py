#!/usr/bin/env python3
"""Read-only Git/worktree inventory. Does not fetch or infer release approval."""
import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def run(repo, *args, allowed=(0,)):
    result = subprocess.run(
        ['git', '--no-optional-locks', '-C', str(repo), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0'},
    )
    if result.returncode not in allowed:
        raise RuntimeError(result.stderr.decode('utf-8', 'replace').strip())
    return result


def output(repo, *args):
    return run(repo, *args).stdout.decode('utf-8', 'replace').strip()


def changes(repo):
    entries = run(repo, 'status', '--porcelain=v1', '-z', '--untracked-files=all').stdout.split(b'\0')
    result, index = [], 0
    while index < len(entries):
        entry = entries[index]
        index += 1
        if not entry:
            continue
        status = entry[:2].decode('ascii')
        record = {'status': status, 'path': entry[3:].decode('utf-8', 'replace')}
        if 'R' in status or 'C' in status:
            record['originalPath'] = entries[index].decode('utf-8', 'replace')
            index += 1
        result.append(record)
    return result


def operation(worktree_path):
    def read(path):
        try:
            return path.read_text().strip()
        except OSError:
            return None

    for marker in ('rebase-merge', 'rebase-apply', 'MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'sequencer'):
        path = Path(output(worktree_path, 'rev-parse', '--git-path', marker))
        if not path.is_absolute():
            path = Path(worktree_path) / path
        if not path.exists():
            continue
        if marker.startswith('rebase-'):
            if marker == 'rebase-apply' and (path / 'applying').exists():
                continue
            result = {'type': 'rebase'}
            for key, name in (('branch', 'head-name'), ('onto', 'onto')):
                value = read(path / name)
                if value:
                    result[key] = value
            return result
        if marker == 'sequencer':
            todo = read(path / 'todo')
            command = todo.splitlines()[0].split() if todo else []
            return {'type': {'pick': 'cherry-pick', 'revert': 'revert'}.get(command[0] if command else '', 'sequencer')}
        result = {'type': {'MERGE_HEAD': 'merge', 'CHERRY_PICK_HEAD': 'cherry-pick', 'REVERT_HEAD': 'revert'}[marker]}
        value = read(path)
        if value:
            result.update({'mergeHeads': value.splitlines()} if marker == 'MERGE_HEAD' else {'commit': value})
        return result
    return None


def inventory(repo, release_ref=None):
    output(repo, 'rev-parse', '--git-dir')
    release_sha = output(repo, 'rev-parse', '--verify', '--end-of-options', release_ref + '^{commit}') if release_ref else None
    remote_tips = {}
    for line in output(repo, 'for-each-ref', '--format=%(refname)%00%(objectname)', 'refs/remotes').splitlines():
        name, sha = line.split('\0')
        remote_tips[name] = sha
    worktrees = []
    raw = run(repo, 'worktree', 'list', '--porcelain', '-z').stdout.decode('utf-8', 'replace')
    for block in raw.split('\0\0'):
        if not block.strip('\0'):
            continue
        record = {}
        for field in block.strip('\0').split('\0'):
            key, _, value = field.partition(' ')
            record[key] = value or True
        if 'worktree' in record and not record.get('bare'):
            try:
                record['changes'] = changes(record['worktree'])
                record['dirty'] = bool(record['changes'])
                current_operation = operation(record['worktree'])
                if current_operation:
                    record['operation'] = current_operation
                if record.get('detached'):
                    record['commitsOnNoLocalBranchOrCachedRemote'] = int(output(record['worktree'], 'rev-list', '--count', record['HEAD'], '--not', '--branches', '--remotes'))
            except RuntimeError as error:
                record['inspectionError'] = str(error)
        worktrees.append(record)
    branches = []
    fmt = '--format=%(refname)%00%(objectname)%00%(upstream)%00%(committerdate:iso-strict)'
    for line in output(repo, 'for-each-ref', fmt, 'refs/heads').splitlines():
        ref, sha, upstream, committed_at = line.split('\0')
        row = {
            'branch': ref.removeprefix('refs/heads/'), 'commit': sha,
            'lastCommitAt': committed_at, 'upstream': upstream or None,
            'upstreamLocallyPresent': None, 'aheadOfUpstream': None, 'behindUpstream': None,
            'matchingCachedRemoteTips': [name for name, value in remote_tips.items() if value == sha],
            'commitsAbsentFromCachedRemotes': int(output(repo, 'rev-list', '--count', sha, '--not', '--remotes')),
            'worktrees': [w['worktree'] for w in worktrees if w.get('branch') == ref],
            'rebasingIn': [w['worktree'] for w in worktrees if (w.get('operation') or {}).get('branch') == ref],
            'fullyContainedInReleaseHistory': None,
        }
        if upstream:
            exists = run(repo, 'show-ref', '--verify', '--quiet', upstream, allowed=(0, 1)).returncode == 0
            row['upstreamLocallyPresent'] = exists
            if exists:
                behind, ahead = output(repo, 'rev-list', '--left-right', '--count', upstream + '...' + sha).split()
                row.update(aheadOfUpstream=int(ahead), behindUpstream=int(behind))
        if release_sha:
            result = run(repo, 'merge-base', '--is-ancestor', sha, release_sha, allowed=(0, 1))
            row['fullyContainedInReleaseHistory'] = result.returncode == 0
        branches.append(row)
    entries = []
    if run(repo, 'show-ref', '--verify', '--quiet', 'refs/stash', allowed=(0, 1)).returncode == 0:
        entries = run(repo, 'log', '-g', '-z', '--format=%gd%x00%H%x00%cI%x00%gs', 'refs/stash').stdout.decode('utf-8', 'replace').split('\0')
    stashes = [dict(zip(('ref', 'commit', 'createdAt', 'message'), entries[index:index + 4])) for index in range(0, len(entries) - 1, 4)]
    return {
        'observedAt': datetime.now(timezone.utc).isoformat(), 'repository': str(Path(repo).resolve()),
        'releaseRef': release_ref, 'releaseCommit': release_sha,
        'remoteState': 'Cached local refs only; no fetch or remote-server verification performed.',
        'limitations': 'History containment does not detect squash-equivalent work. Ignored artifacts are not inventoried. Stash and operation detection read local state only and do not establish ownership. No branch is classified as abandoned or safe to delete.',
        'worktrees': worktrees, 'branches': branches, 'stashes': stashes,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', nargs='?', default='.')
    parser.add_argument('--release-ref', help='Explicit known release/integration ref; no branch name is assumed.')
    args = parser.parse_args()
    try:
        print(json.dumps(inventory(args.repository, args.release_ref), indent=2))
    except (RuntimeError, OSError) as error:
        parser.exit(2, 'Inventory failed: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
