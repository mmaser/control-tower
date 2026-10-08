# Control Tower

**An air traffic controller for your coding sessions.**

### Your agents are making progress. But are they working together?

One session is fixing a bug. Another is building a feature. A third is ready to release—and may not know about either of the others. Meanwhile, you’re carrying updates between sessions, tracking unfinished branches, and trying to keep changes from landing in the wrong order.

Control Tower gives your project an air traffic controller: one session that connects the work across your agents, keeps track of ownership and dependencies, and coordinates what ships next. You keep building; it helps keep everyone working from the same picture.

[v1.0](https://github.com/mmaser/control-tower/releases/tag/v1.0.0) · [Quick start](#quick-start) · [Setup by app](SETUP.md) · [Examples](#examples) · [Feedback](CONTRIBUTING.md)

## How I use it

I keep a session called **DevOps** in every project and run Control Tower there. It’s the project’s air traffic controller—the place I check for what’s happening across the other sessions and what’s ready to ship.

During setup, Control Tower adds the coordination agreement to the project’s instructions and brings existing sessions on board through messages or handoffs. New sessions pick up that agreement from the project instructions. Each session keeps doing its own work, with DevOps coordinating the shared decisions and release order.

![Codex project sidebar showing a DevOps chat alongside a chat reviewing code comments.](assets/codex-project-chats.png)

*One place to check what is happening across the project.*

![A working chat reports that its change is committed and checks pass; DevOps is routing it through the release owner while it awaits integration confirmation.](assets/codex-ready-for-integration.png)

*The working chat has finished its change. Control Tower coordinates when it joins the release.*

<details>
<summary>Two more examples of updates in working chats</summary>

![A working chat reports handing its commit to DevOps, with deployment pending to avoid collisions.](assets/codex-release-handoff.png)

*The handoff is complete; deployment is still pending.*

![A working chat reports confirmation that the release owner has its change, with a place in the current release or immediately afterward.](assets/codex-release-queue.png)

*The change has an owner and a place in the release queue.*

</details>

These illustrative examples are adapted from the Codex workflow that informed Control Tower.

## Quick start

Start with one project. Your coding agent can handle the setup details.

1. **Get the package.** Download and extract [`control-tower-release.zip`](https://github.com/mmaser/control-tower/releases/download/v1.0.0/control-tower-release.zip), or download this repository through **Code → Download ZIP**. Find the folder containing `SKILL.md` and `SETUP.md`; a GitHub source download may call it `control-tower-main`.
2. **Open your project** in Codex or Claude Code, in the desktop app or CLI. In the chat you want to coordinate the project, paste the prompt below, replacing `[folder location]` with that extracted folder's location.
3. **Check the setup report.** It should identify the loaded version, the project agreement, and which existing sessions have acknowledged it. If the coordinator cannot contact them, paste its prepared handoff into those chats.

```text
Set up Control Tower for this project using the package at [folder location].
Read its SETUP.md and handle the applicable steps. Install it for this project
if needed and verify the loaded version. Use this chat as coordinator unless
one already exists; retain the existing coordinator unless I explicitly request
a handover. Update the project's instructions and coordinate its existing chats
so they recognize the agreement. Preserve existing work, installed skills,
and publication permissions. Tell me what's ready and which sessions still
need attention.
```

Then try a real task: **“Check what our active sessions are working on and recommend the next merge order.”**

**Claude Desktop general chat or Cowork:** use the [account-upload steps](SETUP.md#claude-desktop-general-chat) first. General chat and the Code tab have different setup routes.

The [full setup guide](SETUP.md) covers desktop and CLI, new and existing projects, project-wide adoption, optional global use, and checks that the other sessions recognize the coordinator. Installing the skill alone does not bring existing chats into the agreement.

## What it helps with

- **Sessions working past each other.** Connect ownership, dependencies, and release readiness across chats.
- **Changes that need to land in order.** Coordinate an app update with its backend, or keep a later website release from overwriting an earlier fix.
- **Branches nobody remembers.** Investigate orphaned-looking branches, unfinished merges, and commits that may already have shipped, while preserving uncertain work.
- **Losing the thread.** Keep a current project record of what is saved, recoverable, approved, released, or waiting on someone.

You keep control of product direction and publication authority. Control Tower follows your existing tools and release procedures, and carries out authorized routine work without repeatedly asking for the same approval.

## Examples

These fictional examples show how coordination can work across different projects. Think of the coordinator as air traffic control for your coding sessions: it helps establish what is ready, what depends on something else, and whose turn it is to release, while independent work keeps moving.

### An iOS app and its backend

> “One chat has the next iOS build ready, and another has the API change it needs. Coordinate them. You can back up the work, release the compatible API change, and send build 42 to our TestFlight testers. Wait for my approval before submitting it to the App Store.”

The coordinator checks the two candidates, existing ownership, account targets, release triggers, and evidence that the API change supports the currently released app. It preserves unfinished work and tests the relevant combined behavior. If the evidence supports the authorized plan, it coordinates the API release, verifies that target, and distributes the exact app build to testers. It records the remaining store-submission boundary.

Its report might be:

> “The API change is deployed and checked against the current app. Build 42 is available to testers; it has not been submitted to the store. Both source revisions are backed up and recovery is verified. Your next decision is whether to submit build 42.”

If it cannot observe tester availability, it says so. If a command times out, it checks whether the operation succeeded before repeating it. If another release intervenes, it reconciles the new baseline before proceeding.

### A website with several changes ready to ship

> “Three chats are working on our website. The checkout fix is urgent and approved to go live. The new product page is also approved, but the homepage redesign is still an experiment. Coordinate the chats and get the approved changes out.”

The coordinator identifies who owns each change and whether any files or release steps overlap. It checks whether the checkout fix and product page depend on each other, then agrees on a release order with the authorized sessions. In this example, the fix can ship first. Before releasing the product page, it incorporates that fix into the candidate and checks the combined result. The unfinished redesign remains preserved separately, and its chat can keep working.

Its report might be:

> “The checkout fix is live and verified. The product page then shipped with that fix included, so it didn't replace the repair with older code. The homepage experiment is backed up and remains private. Both releases are complete; neither is blocking the next change.”

### Branches and commits that have become hard to untangle

> “I have branches left over from several chats, a merge that never finished, and changes I thought we'd already shipped. Figure out what belongs where. Back up anything useful, prepare the right merge order, and leave uncertain work alone.”

The coordinator checks branch history, actual released code, unfinished merges, and uncommitted work, then reconciles ownership with the available sessions. A branch that looks orphaned may still contain active work; an old commit may already have shipped through a different merge. It distinguishes those cases before proposing cleanup.

Suppose a settings-screen change depends on a data-model change that hasn't landed, while a separate fix is already in production. The coordinator prepares the data-model change first, then the settings screen, checks the combined candidate, and avoids applying the shipped fix again. It preserves the interrupted merge and establishes its owner before continuing or replacing that work. Preparation does not itself publish the result or delete branches.

Its report might be:

> “The settings screen needs the data-model change first. I've prepared and checked that combined candidate. The other fix is already live. The interrupted merge is preserved for its owner, and one branch still has unclear ownership, so I've left it intact. Useful work is backed up; nothing has been deleted or published.”

## Where it works

Where your tools support it and you authorize it, the coordinator talks directly with the other sessions; otherwise, it prepares handoffs you can pass along.

The setup guide covers Codex desktop and CLI, Claude Desktop's Code tab, Claude Code CLI, and general Claude chat. The local skill files are shared between desktop and CLI within each tool when they use the same environment. Their access to other sessions can differ.

Claude Desktop's Code tab also documents session inspection and messaging, so the same coordination approach can apply there. Check visibility in your actual environment; use explicit handoffs where direct messaging is unavailable. [Claude session coordination](https://code.claude.com/docs/en/desktop#work-across-sessions)

Developed through hands-on use in Codex across active projects. Includes setup guidance for Claude and coordination guidance for web, iOS, Android, and backend work. Experience across those environments will inform future updates.

## Requirements and limits

Your agent needs access to the skill and its supporting files. To operate on your project, it also needs the relevant repository and provider tools. The optional read-only Git inventory helper needs Git and Python 3.9 or newer.

Control Tower supplies instructions, not an enforced merge queue or background service. Other chats must recognize the project agreement, and the coordinator can only verify what its tools can observe. Monitoring between turns requires a separately requested host automation.

The Git helper uses cached remote refs, omits ignored artifacts, and never decides that a branch is abandoned or safe to delete. Its output is a starting point for investigation, not proof of remote recovery.

## Inside the package

- [SKILL.md](SKILL.md) — operating instructions for the coordinator.
- [SETUP.md](SETUP.md) — installation and adoption across project sessions.
- [Supporting references](references/) — conditional setup, capability limits, release contexts, and project records.
- [Git inventory helper](scripts/git_inventory.py) — a read-only starting point for inspecting branches and worktrees.

## Feedback and updates

Feedback is welcome—especially what worked, what got in the way, and what would make Control Tower more useful. [Open an issue](https://github.com/mmaser/control-tower/issues) or see [how to report a problem or suggest a change](CONTRIBUTING.md).

Releases will identify their version and changes. Updating installed files does not guarantee that an active chat reloads them; verify the version and use a fresh session when needed.

Created by [Mike Maser](https://github.com/mmaser), while learning what happens when several AI coding chats all have good intentions at once.

## License

[MIT](LICENSE) · Copyright © 2026 Mike Maser.
