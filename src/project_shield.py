import json
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Task:
    id: int
    name: str
    scope_id: int

@dataclass
class Issue:
    id: int
    name: str
    scope_id: int

@dataclass
class ScopeDefinition:
    id: int
    name: str
    tasks: List[Task] = field(default_factory=list)
    issues: List[Issue] = field(default_factory=list)

class ProjectShield:
    def __init__(self):
        self.scope_definitions = {}
        self.tasks = {}
        self.issues = {}

    def create_scope_definition(self, name: str) -> ScopeDefinition:
        scope_id = len(self.scope_definitions) + 1
        scope_definition = ScopeDefinition(id=scope_id, name=name)
        self.scope_definitions[scope_id] = scope_definition
        return scope_definition

    def edit_scope_definition(self, scope_id: int, name: str) -> ScopeDefinition:
        if scope_id in self.scope_definitions:
            self.scope_definitions[scope_id].name = name
            return self.scope_definitions[scope_id]
        else:
            raise ValueError("Scope definition not found")

    def assign_task_to_scope(self, task_id: int, scope_id: int) -> Task:
        if scope_id in self.scope_definitions:
            task = Task(id=task_id, name=f"Task {task_id}", scope_id=scope_id)
            self.tasks[task_id] = task
            self.scope_definitions[scope_id].tasks.append(task)
            return task
        else:
            raise ValueError("Scope definition not found")

    def assign_issue_to_scope(self, issue_id: int, scope_id: int) -> Issue:
        if scope_id in self.scope_definitions:
            issue = Issue(id=issue_id, name=f"Issue {issue_id}", scope_id=scope_id)
            self.issues[issue_id] = issue
            self.scope_definitions[scope_id].issues.append(issue)
            return issue
        else:
            raise ValueError("Scope definition not found")

    def track_scope_progress(self, scope_id: int) -> Dict:
        if scope_id in self.scope_definitions:
            scope_definition = self.scope_definitions[scope_id]
            tasks_completed = sum(1 for task in scope_definition.tasks if task.id % 2 == 0)
            issues_resolved = sum(1 for issue in scope_definition.issues if issue.id % 2 == 0)
            return {
                "tasks_completed": tasks_completed,
                "issues_resolved": issues_resolved,
                "total_tasks": len(scope_definition.tasks),
                "total_issues": len(scope_definition.issues)
            }
        else:
            raise ValueError("Scope definition not found")
