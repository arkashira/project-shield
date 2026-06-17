# STORIES.md  

## Project Overview  
**project‑shield** – a lightweight SaaS/CLI tool for open‑source maintainers and contributors that helps define, visualise, and enforce a project’s scope. It prevents scope creep, aligns expectations, and reduces contributor frustration by providing clear, versioned “scope contracts” and automated alerts.

---

## Epics & Backlog  

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Scope Definition & Versioning** | Enable maintainers to create, edit, and publish a formal scope contract for each release. | 1 |
| **E2 – Contributor Interaction** | Give contributors a simple way to view the current scope, propose changes, and receive feedback. | 2 |
| **E3 – Automated Scope Enforcement** | Detect when PRs/Issues fall outside the defined scope and surface warnings. | 3 |
| **E4 – Notification & Reporting** | Notify maintainers/contributors of scope violations and generate periodic compliance reports. | 4 |
| **E5 – Integration & Extensibility** | Provide CI/CD and GitHub/GitLab integrations; expose a plugin API for custom rules. | 5 |
| **E6 – Analytics Dashboard** | Visualise scope health, churn, and contributor satisfaction metrics. | 6 |

---

## User Stories  

### Epic E1 – Scope Definition & Versioning  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E1‑01** | **As a maintainer, I want to create a new scope contract for a release, so that contributors know exactly what is in‑scope.** | • UI/CLI command `shield scope create <release>` opens an editor with a markdown template.<br>• Contract is saved as `SHIELD_SCOPE_<release>.md` in the repo root.<br>• Commit includes a signed SHA‑256 hash stored in `shield.json` for integrity.<br>• The new scope appears in the “Current Scope” view. |
| **E1‑02** | **As a maintainer, I want to version scope contracts, so that historic scope can be audited.** | • Each `shield scope create` automatically tags the commit with `shield‑v<semver>`.<br>• `shield scope history` lists all versions with timestamps, author, and diff preview.<br>• Ability to roll back to a previous version via `shield scope revert <tag>`. |
| **E1‑03** | **As a contributor, I want to view the active scope contract in the repository UI, so that I can quickly verify what is allowed.** | • A badge “Scope: vX.Y.Z” appears on the repo’s README.<br>• Clicking the badge opens the rendered markdown of the latest `SHIELD_SCOPE_*.md`.<br>• The same view is available via `shield scope view`. |
| **E1‑04** | **As a maintainer, I want to lock a scope contract after release, so that accidental edits are prevented.** | • `shield scope lock <release>` marks the contract as immutable.<br>• Locked contracts reject any push that modifies the file unless a maintainer uses `shield scope unlock`. |
| **E1‑05** | **As a maintainer, I want to import an existing `CODE_OF_CONDUCT` or `CONTRIBUTING` file as a baseline scope, so that I don’t duplicate effort.** | • `shield scope import <path>` parses headings and creates a scoped contract preserving relevant sections.<br>• Imported content is highlighted as “auto‑generated” and editable. |

### Epic E2 – Contributor Interaction  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E2‑01** | **As a contributor, I want to propose a scope change when filing an issue, so that the maintainer can evaluate it formally.** | • Issue template includes a “Scope Impact” section with a toggle (In‑scope / Out‑of‑scope / New‑scope).<br>• Submitting the issue creates a linked draft scope change stored in `.shield/proposals/`. |
| **E2‑02** | **As a maintainer, I want to review and accept/reject scope proposals, so that the project’s boundaries evolve deliberately.** | • `shield proposal list` shows pending proposals with author, description, and diff.<br>• `shield proposal approve <id>` merges the proposal into the active scope and bumps the version.<br>• Rejection adds a comment to the originating issue and archives the proposal. |
| **E2‑03** | **As a contributor, I want real‑time feedback when my PR touches out‑of‑scope files, so I can adjust before review.** | • During PR creation, the GitHub Action runs `shield check` and posts a comment “⚠️ This PR modifies out‑of‑scope areas: …”.<br>• The comment includes a link to the relevant scope clause. |

### Epic E3 – Automated Scope Enforcement  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E3‑01** | **As a CI pipeline, I need to fail builds that introduce out‑of‑scope changes, so that violations are caught early.** | • GitHub Action `shield/enforce` runs on `push` and `pull_request` events.<br>• If any changed file is flagged out‑of‑scope, the job exits with status 1 and prints the offending paths. |
| **E3‑02** | **As a maintainer, I want a configurable rule set (e.g., file patterns, module boundaries), so that enforcement matches project architecture.** | • `shield.config.yaml` supports `allow:`, `deny:`, and `exceptions:` sections using glob patterns.<br>• Changes to the config trigger a re‑evaluation of existing PRs. |
| **E3‑03** | **As a contributor, I want to override a scope warning with a maintainer’s explicit approval, so that exceptional work can proceed.** | • Adding a comment `@shield approve` on the PR creates a temporary exemption record valid for that PR only.<br>• The exemption is logged in `shield.log` with timestamp and approver. |

### Epic E4 – Notification & Reporting  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E4‑01** | **As a maintainer, I want email/slack notifications for scope violations, so I can act quickly.** | • Configurable webhook URL in `shield.config.yaml`.<br>• On each violation, a payload with PR/issue link, violated clause, and severity is sent. |
| **E4‑02** | **As a project lead, I want a weekly compliance report, so I can track scope adherence over time.** | • `shield report --weekly` generates a markdown summary with counts of violations, resolved proposals, and scope churn.<br>• Report is auto‑posted to a designated repo issue or Slack channel. |
| **E4‑03** | **As a maintainer, I want to silence notifications for a specific PR after approval, so I’m not spammed.** | • Adding the label `shield‑silenced` to a PR suppresses further alerts for that PR. |

### Epic E5 – Integration & Extensibility  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E5‑01** | **As a DevOps engineer, I want a Docker image with the Shield CLI pre‑installed, so I can run it in any CI environment.** | • `Dockerfile` builds `arkashira/project-shield:latest` exposing the `shield` binary.<br>• Image size < 150 MB and passes `docker run --rm` health check. |
| **E5‑02** | **As a maintainer, I want a GitHub App that automatically adds the “Scope” badge to PRs, so visibility is always high.** | • App installs via `shield-app` marketplace.<br>• On PR open, the app comments with the current scope version badge. |
| **E5‑03** | **As a power user, I want a plugin API to add custom validation rules (e.g., license compliance), so Shield can be extended.** | • `shield plugin register <path>` loads a Python module exposing `validate(changed_files, scope) -> List[Violation]`.<br>• Plugins are sandboxed and listed via `shield plugin list`. |

### Epic E6 – Analytics Dashboard  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E6‑01** | **As a maintainer, I want a web dashboard showing scope health metrics, so I can monitor project stability.** | • Dashboard reachable at `/shield/dashboard` after `shield serve`.<br>• Shows: total violations (last 30 days), average time to resolve proposals, and scope churn % per release. |
| **E6‑02** | **As a contributor, I want to see my personal “scope compliance” score, so I can improve my contributions.** | • Authenticated view lists user’s PRs with compliance status and a simple score (0‑100). |
| **E6‑03** | **As a senior manager, I want exportable CSV/JSON data for all scope events, so I can feed it into BI tools.** | • `shield export --format csv` produces a file with columns: timestamp, event_type, author, PR/issue ID, violated_clause. |

---

## MVP Ordering (Top‑Down)  

1. **E1‑01, E1‑02, E1‑03** – Core scope creation & visibility.  
2. **E3‑01, E3‑02** – Automated enforcement in CI.  
3. **E2‑01, E2‑02** – Proposal workflow for contributors.  
4. **E4‑01** – Real‑time notifications.  
5. **E5‑01** – Docker image for CI portability.  
6. **E1‑04, E1‑05** – Locking & import helpers.  
7. **E4‑02, E4‑03** – Reporting & silencing.  
8. **E5‑02, E5‑03** – GitHub App & plugin extensibility.  
9. **E6‑01, E6‑02, E6‑03** – Analytics dashboard and export.  

All stories are written to be **shippable** with clear acceptance criteria, enabling incremental delivery while delivering immediate value to open‑source maintainers and contributors.
