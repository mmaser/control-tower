# Release contexts

Use only the sections relevant to the component being released and its dependencies. These are coordination checks, not provider command recipes. Follow existing project workflows and available provider-specific guidance; verify current provider rules when they affect the action. Resolve missing authority or target identity before that action, while continuing independent preparation.

## Websites

Identify which action builds, deploys, or moves traffic, including automatic Git triggers and pending deployments. Record the source/artifact and actual traffic target. A preview, ready build, and published domain may represent different revisions. Verify changed behavior on the intended domain and relevant access controls. Before reverting traffic, confirm that the earlier deployment remains compatible with current data, configuration, and APIs and will not overwrite a newer valid release.

## iOS and Android apps

Identify the exact app, provider account, bundle/package identifier, platform, version/build identifier, signed artifact provenance, and destination channel or track. Check the supported build/signing procedure and secret-store references; do not copy signing material or credentials into records. An upload or signing account may differ from the account used to submit or release.

Distinguish building, uploading, distributing to testers, submitting for review, provider approval, publication, rollout, and observed adoption. Check actual release settings before submission: provider approval may trigger automatic publication. Human approval of a preview or test build does not imply authority for store release. Do not silently change release settings to bypass an unresolved boundary.

Verify the intended build's processing/review state, tester or public availability, rollout scope, and relevant behavior at the level tools allow. Record unavailable evidence honestly. Store availability does not prove that all users have installed the update. Old and new clients may coexist; check backend compatibility and any relevant local-data migration.

Choose a supported recovery action before release. Halting distribution, disabling an existing feature flag, and submitting a corrective build have different effects. Do not claim that pausing a rollout restores existing installations. Confirm what the provider currently permits and whether affected users need a new build. Preserve build provenance and keep an accountable owner for the next store transition; waiting for review does not reserve unrelated project releases.

## Backend services and workers

Identify the service/worker, artifact or image revision, environment, traffic or job-processing target, configuration, and relevant schema/data changes. A successful deployment does not prove that traffic moved, workers adopted the new version, or queued jobs completed. Verify the actual execution path and meaningful behavior; use existing health/error evidence when available.

Determine compatibility with deployed clients, peer services, old workers, queued payloads, and persisted data. For schema changes, establish the migration order, how long old/new versions must coexist, and which transitions are reversible. Prefer a compatible staged transition when needed; do not assume reverting code reverts data or that restoring a database is an acceptable default. A data restore can discard newer writes and needs explicit scope and recovery evidence.

Inspect migration/job state after interrupted commands before repeating them. Establish whether retries are safe and how partial effects will be reconciled. Use the project's recovery method and authority; if reversibility or outcome remains unknown, hold that action and continue diagnosis.

## Products with several components

Record only dependencies relevant to this release. A backend prerequisite may need to ship before a mobile build; incompatible schema removal may need to wait while older clients remain active. Verify those assumptions rather than choosing a universal platform order. Keep independent components moving, while serializing actions that share a target, migration, contract, or other contested dependency. Report state by component when one “live” label would conceal important differences.

## Other release types

For packages or other targets, establish artifact identity, publication triggers, consumers, verification, and supported recovery through the project's workflow. Do not apply website rollback assumptions to immutable published artifacts. If a new platform adds no new coordination constraint, do not invent another mandatory profile.

## Provider references

These sources informed the review candidate on October 8, 2026; they are not a substitute for checking the current project and provider state.

- [Apple release options](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option/)
- [Apple corrective version guidance](https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version)
- [Google Play staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149)
- [Cloud Run traffic and rollback behavior](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)
