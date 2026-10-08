# Capabilities and fallbacks

Use when the required tools, visibility, or access are uncertain. Check what the current host actually exposes; do not infer capability from a product name or prescribe a new service solely to reproduce another host's workflow. Capability and authorization are separate requirements.

Identify the current surface and execution environment: desktop Code workspace, terminal CLI, general chat, or remote runtime. The [setup guide](../SETUP.md) distinguishes their installation and instruction entry points. Shared skill files or account synchronization do not establish shared session visibility, messaging, repository access, or project authority. Verify each separately; record the actual loaded source when local and account copies coexist.

| Missing or limited capability | Useful behavior |
| --- | --- |
| Local repository or shell access | Inspect available repository APIs or user-provided evidence. Report its revision and freshness. Do not claim a complete working-tree inventory or execute the helper without Git and Python. |
| Remote access | Local refs are cached evidence. Prepare local work where authorized; leave remote recovery and current server state unverified. |
| Other-chat inspection | Use durable handoffs or user-supplied updates. Mark session visibility incomplete; absence from the visible list does not establish inactivity. |
| Other-chat messaging | Prepare a concrete handoff for the user to relay. A draft or delivery is not an acknowledgment. Hold only actions whose conflict cannot be resolved; continue independent work. |
| Provider publication or observation | Prepare and check the candidate through available tools. Supply the exact remaining action and evidence needed. Do not report publication or runtime verification from a build log alone. |
| Background execution | Finish with a checkpoint and next step. Do not promise to keep watching. Create automation only when requested and supported. |

Do not switch shared login state, broaden permissions, install infrastructure, or create sessions as an automatic fallback. Use authorized existing tools and supported scoped selectors. When requesting access or a decision, explain the concrete action it enables.

Ownership records and cooperative messages do not enforce exclusion. Recheck actual writers and target state before conflicting mutations; use an existing enforced queue or lock when the project provides one. An expired timestamp or quiet chat alone does not release a hold.

After a host change or skill update, establish which skill files and version the session is using. Do not assume active conversations reload changed instructions. If that cannot be verified, use a fresh session with a current handoff before consequential work. Never self-install or self-update this skill as part of ordinary project operation.
