from project_shield import ProjectShield, ScopeDefinition, Task, Issue

def test_create_scope_definition():
    project_shield = ProjectShield()
    scope_definition = project_shield.create_scope_definition("Test Scope")
    assert scope_definition.name == "Test Scope"
    assert scope_definition.id == 1

def test_edit_scope_definition():
    project_shield = ProjectShield()
    scope_definition = project_shield.create_scope_definition("Test Scope")
    edited_scope_definition = project_shield.edit_scope_definition(1, "Edited Test Scope")
    assert edited_scope_definition.name == "Edited Test Scope"

def test_assign_task_to_scope():
    project_shield = ProjectShield()
    project_shield.create_scope_definition("Test Scope")
    task = project_shield.assign_task_to_scope(1, 1)
    assert task.name == "Task 1"
    assert task.scope_id == 1

def test_assign_issue_to_scope():
    project_shield = ProjectShield()
    project_shield.create_scope_definition("Test Scope")
    issue = project_shield.assign_issue_to_scope(1, 1)
    assert issue.name == "Issue 1"
    assert issue.scope_id == 1

def test_track_scope_progress():
    project_shield = ProjectShield()
    project_shield.create_scope_definition("Test Scope")
    project_shield.assign_task_to_scope(1, 1)
    project_shield.assign_task_to_scope(2, 1)
    project_shield.assign_issue_to_scope(1, 1)
    project_shield.assign_issue_to_scope(2, 1)
    progress = project_shield.track_scope_progress(1)
    assert progress["tasks_completed"] == 1
    assert progress["issues_resolved"] == 1
    assert progress["total_tasks"] == 2
    assert progress["total_issues"] == 2

def test_scope_definition_not_found():
    project_shield = ProjectShield()
    try:
        project_shield.edit_scope_definition(1, "Test Scope")
        assert False
    except ValueError as e:
        assert str(e) == "Scope definition not found"
