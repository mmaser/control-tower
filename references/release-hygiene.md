# Release and repository hygiene

Use the subset relevant to the project; a documentation edit does not require a full application certification. Follow applicable provider-specific guidance, using its skill when available. Web hosts, app stores, package registries, and internal services have different publication triggers and evidence. Use the relevant section of [release contexts](release-contexts.md) for those differences.

## Before integration

- Confirm repository/project/environment identities. Inspect Git status, branches, worktrees, upstreams and actual remote refs. Never assume local `main` is the approved production source.
- Verify the actual execution path’s authenticated principal and account/tenant against the project account map, including the target project and environment. Use supported scoped selection; do not infer CLI or CI identity from a browser session. Record corrected mappings and procedures in the project playbook.
- Identify active owners and what each is editing, integrating, or publishing. Check current target state independently of a chat's stale status; include in-flight submissions, deployments, migrations, and configuration changes where relevant.
- Establish component dependencies, compatibility requirements, and supported recovery. A source rollback, traffic rollback, rollout halt, corrective app build, and data restore have different effects and authority requirements.
- Verify the approved scope. Separate operational authorization from approval of candidate content. Preserve unrelated staged/unstaged files and local commits.
- Choose an isolated integration checkout when shared work could collide. Do not reset an existing worker's checkout to obtain a clean release tree.

## Candidate and publication

- Integrate the current approved base and only the intended change. Preserve fixes from intervening releases; resolving a Git conflict is not proof of correct behavior.
- Run checks appropriate to changed behavior and project policy. Compare deployed code or asset hashes where exact artifacts matter. Keep original/versioned source recoverable.
- Confirm publication triggers and release settings, including automatic deployments or release after store approval. A manual promotion followed by an older automatic deployment can undo the newer release. Use one coordinated path per conflicting target and account for in-flight operations.
- Immediately before the consequential action, compare current integration, target, and dependency state with the agreed baseline. If relevant state changed, reconcile it and rerun affected checks; do not blindly retry a rejected push or repeat a submission.
- For an ambiguous command result, use the interruption recovery check below. A build marked ready may still have no traffic or distribution.
- Verify the intended source/build, actual target or channel, resulting availability or traffic, changed behavior, and relevant access controls. Distinguish local tests, tester/staging checks, provider state, and runtime verification in the handoff.
- If verification fails, preserve evidence, hold conflicting follow-on actions, and use an authorized recovery only after confirming its compatibility and that it will not replace a newer valid release. Escalate unresolved direction or authority questions; continue independent diagnosis.

## Resume after interruption or uncertain outcome

1. Reconstruct the last intended action, exact candidate/target, authority, and named owner from current records and available command evidence. Do not infer completion or cancellation from the previous chat ending.
2. Inspect surviving processes/jobs, current remote refs, provider operations, and actual traffic/distribution or migration state as relevant. A client timeout does not prove the external operation failed. Do not stop another owner's process merely to obtain a clean restart.
3. Classify the action as completed, still in progress, failed before effects, partially applied, or unknown, supported by evidence. Reconcile with any newer release or ownership handoff before acting.
4. Verify a completed result; observe an in-progress operation within the authorized task; retry only when its effects and retry semantics make that appropriate. For partial or unknown effects, continue diagnosis and hold only the unsafe retry/recovery. Seek a user decision when the resolution would change scope or authority.
5. Record the reconciled state and next owner. Clear or transfer holds with an observable exit condition. Do not promise later observation without an existing requested automation.

## Branch and worktree lifecycle

The inventory helper does not fetch, push, modify files, or delete anything. Its remote refs are cached observations. A branch marked fully contained in a release ref is only a history fact; it may still have active uncommitted work. Squash/rebased integration can leave ancestry checks negative even when content was shipped; review the integration evidence before labeling that work outstanding.

For each candidate cleanup item:

1. Identify owner, worktree use, upstream state, unique commits, uncommitted/untracked files, and needed ignored artifacts.
2. Classify active / awaiting review / blocked / integrated / archived / potentially stale. Unknown ownership stays unresolved, not abandoned.
3. Prove recovery remotely: verify the expected commit/ref or archived snapshot and relevant file content. A local commit or successful command log alone is insufficient.
4. Check existing authorization for the proposed cleanup. Delete/retire only when scope and recoverability are clear; avoid force deletion and force-pushing. For managed worktrees, use their supported archival mechanism when available, preserving needed ignored files separately.
5. Record the recovery location and what was retired. Keep essential evidence outside any folder being removed.

For WIP that must remain untouched, use an isolated copy or a separate temporary Git index for a point-in-time snapshot; never stage an entire active shared checkout. Exclude secrets, dependencies and irrelevant build outputs. Handle large files through the project's artifact storage. Review resulting content and disable unintended deployment before pushing a backup branch. A backup does not grant approval to publish its contents.

## Finish without leaving another traffic jam

Checkpoint owned operational changes within the task's authorization and the project's workflow. A local-only task does not imply a remote push; a documentation push may itself publish. Record outstanding work with an owner and next step, release browser/environment reservations, and explicitly clear temporary holds or transfer them with an observable exit condition. Prefer conditional sequencing over requiring the user to approve routine operations again. Do not leave a chat indefinitely waiting for a coordinator that has already ended its turn.
