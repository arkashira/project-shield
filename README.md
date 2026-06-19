# Project Shield
Project Shield is a Python project for managing project scope definitions, tasks, and issues.

## Features
* Create and edit project scope definitions
* Assign tasks and issues to specific scope definitions
* Track and visualize scope progress

## Usage
1. Create a new project scope definition using `project_shield.create_scope_definition("Test Scope")`.
2. Assign tasks and issues to the scope definition using `project_shield.assign_task_to_scope(1, 1)` and `project_shield.assign_issue_to_scope(1, 1)`.
3. Track scope progress using `project_shield.track_scope_progress(1)`.

## Testing
Run tests using `pytest` command.
