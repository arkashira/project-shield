from project_shield import ProjectShield, Commit
import pytest

def test_get_scope_document():
    scope_document = "This is a scope document"
    commits = [Commit("2022-01-01 12:00:00", "Initial commit")]
    project_shield = ProjectShield(scope_document, commits)
    assert project_shield.get_scope_document() == scope_document

def test_get_commits():
    scope_document = "This is a scope document"
    commits = [Commit("2022-01-01 12:00:00", "Initial commit"), Commit("2022-01-02 12:00:00", "Second commit")]
    project_shield = ProjectShield(scope_document, commits)
    assert len(project_shield.get_commits()) == 2

def test_get_latest_version():
    scope_document = "This is a scope document"
    commits = [Commit("2022-01-01 12:00:00", "Initial commit"), Commit("2022-01-02 12:00:00", "Second commit")]
    project_shield = ProjectShield(scope_document, commits)
    assert project_shield.get_latest_version() == "Second commit"

def test_get_commit_history():
    scope_document = "This is a scope document"
    commits = [Commit("2022-01-01 12:00:00", "Initial commit"), Commit("2022-01-02 12:00:00", "Second commit")]
    project_shield = ProjectShield(scope_document, commits)
    expected_history = [{"timestamp": "2022-01-01 12:00:00", "message": "Initial commit"}, {"timestamp": "2022-01-02 12:00:00", "message": "Second commit"}]
    assert project_shield.get_commit_history() == expected_history

def test_get_latest_version_no_commits():
    scope_document = "This is a scope document"
    commits = []
    project_shield = ProjectShield(scope_document, commits)
    assert project_shield.get_latest_version() == "No commits"
