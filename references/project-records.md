# Project records

Adapt existing conventions; do not create competing sources of truth. Use only fields relevant to the current project and task, not a mandatory questionnaire. Start with observed facts and mark unknown values. The profile is stable configuration, while status is a dated checkpoint that must be refreshed before a release. A checked-in owner field is a coordination record, not an atomic lock.

## PROJECT-OPERATIONS.md template

```markdown
# Project operations

## Sources and environments
- Repository or repositories and remotes:
- Local workspace/checkouts (only if useful; omit machine-specific paths from shared copies):
- Integration branch:
- Release branches/tags:
- Independently released components and relevant dependencies:
- Hosting/build/store provider and project/app identifiers:
- Production targets, domains, or distribution channels/tracks:
- Preview/staging/tester targets and access requirements:
- Publication triggers: Git push / manual promotion / CI / store approval / other
- Release settings and preview/backup-branch distribution policy:
- How to inspect source/build identity, availability, rollout, or traffic:
- Compatibility window for older clients, services, workers, and schemas:

## Accounts and authentication routing
| Execution path / environment | Intended account or tenant | Repository / project identifier | Scoped profile or selector | Safe identity and target check | Verified at / evidence |
| --- | --- | --- | --- | --- | --- |

- Document only paths this project actually uses: Git transport, repository API/CLI, hosting or store CLI/API, signing/upload tools, browser or CI. Their principals may legitimately differ.
- Secret-store references and variable names, never secret values:
- Runtime/toolchain versions or setup prerequisites needed to reproduce releases:
- Known account-selection pitfalls and the verified resolution:

## Responsibilities and authority
- Designated coordinator (stable chat identity/contact) and project scope:
- Supported coordination route and active-session discovery/visibility limits:
- Effective session instruction entry point and canonical current-record source:
- User's operational coordination authorization (source/scope):
- Authority for relevant transitions (test distribution, submission, publication, recovery) and any remaining approval gate:
- Decisions reserved for the user:
- Branch/worktree cleanup policy:
- Shared resources needing temporary exclusive use:
- Handover/unavailable-coordinator procedure:

## Checks and preservation
- Required build/tests and meaningful runtime checks:
- How to verify the actual target/channel and resulting behavior:
- Recovery method, reversibility limits, and known requirements:
- Migration/job retry procedure where relevant:
- WIP backup destinations and how to verify remote recovery:
- Artifact/archive locations, classification and restoration checks:
- Handoff/status location and who updates it:
- Playbook owner, last verification date, and when to recheck account/environment mappings:
```

Keep secrets in configured secret stores or ignored environment files. Authorization notes point to real human authorization; they do not invent or broaden permission. Unknown production triggers or target identity must be resolved before a publication-affecting action, but independent audit work can continue.

For multiple-account environments, verify the credentials used by the actual command or integration. A browser login does not establish the CLI account; Git commit authorship does not establish Git transport or API authentication. Record stable account/project identifiers alongside recognizable names, and a supported scoped selector or safe command example. Do not embed tokens in commands, remote URLs, logs or examples. Keep machine-specific setup in a local companion when appropriate and link it from the shared playbook without copying secrets.

After resolving a setup failure or environment change, record the cause, working procedure and evidence in the existing playbook; replace stale guidance and link detailed diagnostics rather than retaining contradictory instructions. Distinguish observed configuration from intended or unverified setup. Reverify at the relevant action boundary even when a saved mapping exists. A documentation push that triggers deployment follows the same release queue; it does not require an unrelated runtime change.

## PROJECT-STATUS.md template

```markdown
# Project status

Observed at: [date, time, timezone]
Project operations: [link]

## Release state
- Component / environment / channel / URL (only applicable fields):
- Source revision and build/artifact identity:
- Deployment, submission, or release identity:
- Observed processing/review/distribution/traffic state:
- Verification time, evidence, and visibility gaps:
- Relevant compatibility or recovery constraints:
- Later documentation-only revisions, if any:

## Release ownership and queue
| Target / order | Work / owner chat | Source branch or candidate | Authority / checks | Depends on | Next action / hold exit |
| --- | --- | --- | --- | --- | --- |

## Setup adoption (only while introducing or changing coordination)
| Session / checkout | Current agreement source | Read/acknowledgment evidence | Existing owner or in-flight action | Gap / next step |
| --- | --- | --- | --- | --- |

## Recoverability and cleanup
| Work / branch / checkout | Active owner / state | Remote or archive evidence | Unique or unsaved work | Next action |
| --- | --- | --- | --- | --- |

## Questions requiring the user
[Only genuine direction, scope, or authorization questions.]
```

A useful session handoff gives the exact candidate revision/build, owned files, authority evidence, tests, known gaps, expected target state, relevant in-flight operations, and next owner. Record separate components only when relevant; a single-component project does not need a fleet inventory. Avoid copying extensive test logs into the status page; link evidence.

During setup, distinguish skill availability, a configured project agreement, and actual adoption by relevant sessions. A document edit or sent message alone is not acknowledgment. Keep temporary adoption tracking only while useful; after completion, retain a concise evidence checkpoint instead of maintaining another permanent checklist.

## Coordination messages

For a hold: say which environment or shared resource is reserved, by whom, why, what independent work can continue, and exactly what ends the hold. Ask the recipient to acknowledge at a safe boundary; don't claim exclusivity until confirmed or otherwise observed.

For a handoff: supply the current remote integration revision and live identity, the next owner, prerequisite verification, and the exact source to incorporate. Make clear whether a hold is cleared or merely awaiting a dependency. Include both the recipient and coordinator in the durable status so coordination survives either chat ending.
