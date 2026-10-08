# Set up Control Tower

**Install the skill, establish one project coordinator, and bring the other sessions into the agreement.** Installation makes the workflow available; the project agreement tells participants how to coordinate.

This guide accompanies the early preview. The Codex and Claude routes are based on official documentation checked October 8, 2026. Installation and adoption have not yet been exercised. Reviewing these instructions does not install the candidate or change existing projects.

## Quick start

**For most readers: open your project, give your coding agent the extracted package, and use the [copyable quick-start prompt](README.md#quick-start).** It asks the agent to handle installation, project instructions, and existing-session handoffs, then report what is ready.

The rest of this page is a detailed reference. Read only the section you need: [your app and installation](#1-choose-your-app-and-installation-scope), [coordinator setup](#2-establish-the-coordinator-for-this-project), [other sessions](#3-make-the-agreement-visible-to-other-sessions), [verification](#4-verify-that-coordination-is-working), or [global use](#optional-use-the-convention-across-your-projects).

## 1. Choose your app and installation scope

| Where you work | Start here | Does desktop differ from CLI? |
| --- | --- | --- |
| Codex desktop app | [Codex desktop](#codex-desktop) | The same local skill files work in both; starting the session differs. |
| Codex in a terminal | [Codex CLI](#codex-cli) | Uses the folder you open in the terminal. |
| Claude Desktop, Code tab | [Claude Desktop — Code](#claude-desktop-code) | Local Code sessions share skill and instruction files with Claude Code CLI. |
| Claude in a terminal | [Claude Code CLI](#claude-code-cli) | Uses Claude Code's local installation paths. |
| Claude Desktop, general chat or Cowork | [Claude Desktop — general chat](#claude-desktop-general-chat) | Uses account skill upload and project settings; see the sync note below. |

**Start with one project for a pilot.** User scope, sometimes called global, makes the skill available across your projects in that local environment. Each project still needs its own coordinator agreement. Account skills have a separate distribution route described below.

### Prepare the local package

Extract the package ZIP or GitHub source download. Find the folder containing `SKILL.md` and `SETUP.md`. A GitHub source download may name it `control-tower-main`; copy its contents into a folder named `control-tower` at the chosen location, including the references, scripts, and assets:

| Local app | One project | Your projects in that environment |
| --- | --- | --- |
| Codex desktop or CLI | `<project>/.agents/skills/control-tower/` | `~/.agents/skills/control-tower/` |
| Claude Desktop Code or Claude Code CLI | `<project>/.claude/skills/control-tower/` | `~/.claude/skills/control-tower/` |

`<project>` means the top-level folder containing your project's files. `~` means your home folder in the environment running the agent. Folders beginning with a dot may be hidden in your file browser. The resulting path must end in `control-tower/SKILL.md`, without an extra nested `control-tower` folder. These locations follow the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills).

You can ask a coding agent with file access to do this copying. Replace the bracketed values before sending:

> “Install the complete Control Tower package from [local package folder] for [this project only / my user account in this environment], using this tool's supported skill location. Inspect existing copies first and preserve their versions and local changes. Report the installed path and version. Do not change project or global instructions yet.”

Choose one copy per tool and scope where possible. Inspect collisions before copying; do not overwrite an existing installation incidentally. Codex can expose duplicate names. If desktop and CLI use the same user, environment, and project directory, they can share that tool's installation. A remote machine, container, or WSL environment may use a different home and filesystem. Confirm discovery there separately.

For this pilot, check for an older coordinator under a different name too. Explicitly select the candidate and verify its source. If the two cannot be isolated, use a separate test environment; do not disable a global coordinator used by other projects.

### Codex desktop

1. Open the local project folder in the desktop app and start a chat there. The selected folder determines which project files are available. [Codex projects](https://learn.chatgpt.com/docs/projects?surface=app)
2. Use the Codex location above, either by copying the package or sending the installation prompt. No separate CLI installation is needed to follow this desktop route.
3. In a fresh project chat, send the [discovery prompt below](#verify-discovery-before-setup), then continue to step 2 of this guide.

The standalone skill package is the same for desktop and CLI. Chat-management tools can differ, so verify the coordination route in the environment you actually use.

### Codex CLI

“CLI” means the version you run in a terminal. If `codex` is not installed, follow the [official CLI setup](https://learn.chatgpt.com/docs/cli) first.

1. Open a terminal. Replace the example folder with your actual project folder, then run:

   ```sh
   cd "path/to/your/project"
   codex
   ```

2. Use the Codex skill location above or send the installation prompt inside Codex.
3. Start a fresh Codex session in that project if necessary. Use `/skills` to check discovery, or invoke `$control-tower` in the **Codex prompt**, not your terminal's shell. Then send the discovery prompt below. [Codex skills](https://learn.chatgpt.com/docs/build-skills)

If the expected skill is missing after copying it, restart Codex and check the source path again. Continue to step 2 once discovery is confirmed.

### Claude Desktop Code

1. Open Claude Desktop's **Code** tab. Choose **Local** as the environment and select your project folder.
2. Use the Claude Code location above or send the installation prompt in that Code session.
3. Start a fresh local Code session for the project. Type `/` in its prompt box to find Control Tower, or use the skill/slash-command menu. Send the discovery prompt below, then continue to step 2.

Local Desktop Code and Claude Code CLI share skill and `CLAUDE.md` files, so an existing local CLI installation can serve both. Cloud or SSH sessions run elsewhere; verify their source separately. General Claude chat follows the [account-upload route below](#claude-desktop-general-chat). [Claude Desktop Code setup and shared configuration](https://code.claude.com/docs/en/desktop)

### Claude Code CLI

Claude's coding CLI is called **Claude Code**. If `claude` is not installed, follow the [official quickstart](https://code.claude.com/docs/en/quickstart) first.

1. Open a terminal in your project:

   ```sh
   cd "path/to/your/project"
   claude
   ```

2. Use the Claude Code skill location above or send the installation prompt inside Claude Code.
3. In a fresh session, enter `/skills` to inspect available skills. Enter `/control-tower` in the **Claude Code prompt** to invoke it, then send the discovery prompt below. [Claude Code skills](https://code.claude.com/docs/en/skills)

If missing, check the package location and restart the session. Once discovered, continue to step 2.

### Claude Desktop general chat

This route is for general Claude chat or Cowork, rather than a local Code session. Labels can vary as the desktop experience rolls out.

1. Ensure code execution/file creation and skills are available for your account; organization policy may control them.
2. Open **Customize → Skills → + → Create skill → Upload a skill**. Upload `control-tower-release.zip`, containing one `control-tower/` folder with `SKILL.md` directly inside, and enable it. If you downloaded GitHub source instead, ask your coding agent to package that folder in this layout first.
3. Start a chat in the Claude project you want to coordinate, ask Claude to use Control Tower, and send the discovery prompt below. For project-wide adoption, use the project-settings route in step 3.

Enabled account skills can also sync into Claude Code CLI when signed into the same Claude account on supported versions (documented from v2.1.273). Check `/skills` for the `claude.ai sync` source before installing a duplicate. This sync does not apply to API-key or third-party provider authentication, and local CLI skills do not automatically upload back to the account. [Claude skill upload and account sync](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

Loading the skill does not establish access to your local Git checkout, release tools, or other chats. Ask what this session can actually inspect and operate. With limited access, Control Tower can maintain an agreement and prepare handoffs, but must identify which operational checks remain unverified.

### Verify discovery before setup

Use this prompt in whichever app you chose:

> “Locate Control Tower and read its SKILL.md. Report its metadata.version and the exact file path or account-skill source you loaded. Tell me which project files and other sessions you can access. Do not establish or replace a coordinator yet.”

For this preview, expect version `0.1.0-review.2`. Resolve a missing skill, conflicting copy, or wrong version before continuing. Installation, account sync, and shared files do not by themselves connect conversations. Codex and Claude can participate in the same project agreement, but each needs its own discovery check and an available, authorized handoff route.

## 2. Establish the coordinator for this project

Use an existing chat you want to keep as the project's Control Tower. If you want a separate chat, create one or explicitly ask your agent to create it. Other worker sessions keep their existing jobs.

Use this starting prompt once the skill is available:

> “Use Control Tower to set up coordination for this project. Use this chat as coordinator unless one already exists; retain the existing coordinator unless I explicitly request a handover. You may update this project's instructions and coordinate its existing chats to bring them on board. Preserve existing work and publication permissions. Tell me which sessions have confirmed the agreement and which still need attention.”

The coordinator should inspect first, then record the minimum useful agreement in your existing operational documents. It needs its stable chat identity or other reachable address, scope, the current release owner, source of coordination authority, where current status lives, and the boundaries for shared actions. It should retain an existing coordinator unless you requested a handover. There is no need to fill every field in a large template or restate approvals already on record.

**For a new project:** establish the instruction entry point and shared records before several workers begin. If release targets are not known yet, mark them unknown and continue independent work. Setup should not require inventing deployment configuration.

**For an existing project:** inspect active chats, branches/checkouts, owned files, unfinished work, and releases already underway. Preserve their current ownership and release slots while reconciling the agreement. Do not reset files, take over an in-flight release, replace existing rules wholesale, or push documentation through an automatic deployment merely to announce setup.

## 3. Make the agreement visible to other sessions

For Codex, put a short coordination section in the project's existing effective `AGENTS.md`, linking to the agreed operational records. Global guidance is read from the Codex home directory; project and nested instructions can refine it. An override file can replace an `AGENTS.md` at the same level, so inspect the effective instruction chain instead of assuming one filename is active. [Official instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

For **Claude Desktop Code and Claude Code CLI**, add the section to the project's effective `CLAUDE.md` or `.claude/CLAUDE.md`. Use `/memory` to inspect instruction sources. Current Claude Code can also load `AGENTS.md` under documented conditions; retain a working shared setup rather than creating competing instructions. If an existing `CLAUDE.md` needs to import a same-folder `AGENTS.md`, the supported import is `@AGENTS.md`. Verify which files actually load. [Claude Code instruction discovery](https://code.claude.com/docs/en/memory)

For **Claude Desktop general chat**, open the relevant Claude project, choose **Set project instructions**, add the agreement, and save. Make the operating records available through project knowledge or the session's authorized file tools. A repository's instruction file is not a substitute for verifying this chat's context. [Claude project instructions and knowledge](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)

If Codex and Claude both work on a project, their entry points should identify the **same coordinator and current records**. Avoid separate copies of live status that drift apart. If uploaded documents are the available route, name who updates them and verify their freshness before shared actions.

The coordinator can adapt this example after establishing the actual project agreement. Replace the document names when the project already uses different records:

```markdown
## Control Tower coordination

Read the current PROJECT-OPERATIONS.md and PROJECT-STATUS.md before shared work.
The operations record identifies this project's coordinator, contact route,
coordination authority, and current source of these records. Follow its existing
release sequencing and publication boundaries; do not appoint another coordinator.

Report relevant scope, ownership, dependencies, and release readiness through the
authorized coordination route. Before conflicting shared edits, integrations,
publication, or cleanup, confirm the current owner and sequencing agreement.
Continue independent implementation and checks while a specific action is held.

Recheck current records and target state at the shared-action boundary. If the
coordinator is unavailable, preserve progress and prepare a handoff; keep the
conflicting action queued until its existing exit condition is satisfied or the
user explicitly reassigns ownership. Operational coordination does not grant new
publication authority or permission to send Slack messages or emails.
```

Workers need this agreement and current status; they do not all need to run the full coordinator workflow. If the skill is unavailable in a worker's environment, it can still follow the project agreement and report that limitation.

A new chat should load the effective project instructions when it starts. An existing chat needs to read the updated agreement explicitly and acknowledge it. A sent message or changed file alone does not establish adoption.

Where direct chat tools and your authorization exist, the coordinator can send each relevant active session the exact record location and request acknowledgment at a safe boundary. Where they do not, paste this handoff into each active session, replacing the bracketed details:

> “This project now uses [coordinator identity/contact] for operational coordination under [user instruction or agreement reference]. Read [current operations source] and [current status source]. Keep your existing task and preserve your work. Confirm your scope, current release/merge activity, any conflicting hold, and how you will coordinate your next shared action. Do not assume a new publication permission.”

Ensure every active checkout or worktree can access the designated current records. An older branch may contain stale copies. Use an agreed accessible source or a scoped update that respects the checkout owner's work; never reset it just to synchronize instructions. A local file edit does not update a remote checkout or another person's machine.

## 4. Verify that coordination is working

Before relying on the agreement for a shared action, collect these observations:

- The coordinator can identify its skill version, project, authority, current owners, and record locations.
- A fresh worker session identifies the intended coordinator and the relevant shared-action boundary. It does not appoint itself as another tower.
- Relevant existing sessions have read the current agreement and reported their work and in-flight actions. Unreachable or unconfirmed sessions remain explicitly unconfirmed.
- At least one applicable handoff is understood by both sides. Use a harmless readiness report for initial setup, not a production release as a connectivity test.

Mark skill discovery, project configuration, and session adoption separately. A project can be configured while an existing worker still needs attention. Do not hold unrelated work while waiting. These are behavioral checks; matching filenames alone is insufficient.

## Optional: use the convention across your projects

A user-scope install makes the skill available on that host. If you also want a standing default, ask the agent to add a small rule to your tool's global instructions. Changing global instructions requires that scope in your request; the project setup prompt above does not authorize it.

Use the appropriate global entry point, preserving existing instructions:

| Where you work | Where the standing convention belongs |
| --- | --- |
| Codex desktop and CLI | The effective global file in the configured Codex home, normally `~/.codex/AGENTS.md`; check for an active override. [Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| Claude Desktop local Code and Claude Code CLI | `~/.claude/CLAUDE.md` in their shared local environment. [Claude Code instructions](https://code.claude.com/docs/en/memory) |
| Claude Desktop general chat | **Settings → General → Instructions for Claude** in the unified experience. Older layouts may expose Cowork's global instructions separately; inspect the settings available in your version. This is distinct from local Code's instruction file. [Claude Desktop settings transition](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) |

Suggested standing convention:

> “When a project has an established Control Tower, follow that project's coordination agreement and current operating records. Use the coordinator identified there. Global availability of the skill does not create a coordinator or grant release authority. Do not reconfigure unrelated projects.”

New projects still establish their own agreement. Existing projects retain their current coordinator until an explicit handover; do not appoint one chat as the controller for every project. Re-run discovery/adoption checks only when setup or relevant assumptions change, not as a recurring questionnaire.

The skill is not a monitoring service or enforcement mechanism. Closing the coordinator chat does not create a background watcher, and a stale status record is not an exclusive lock. Leave a named next owner or observable exit condition for any hold, and use a requested host automation if later monitoring is actually wanted.
