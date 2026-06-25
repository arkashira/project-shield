import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Scope:
    name: str
    description: str

class ScopeShield:
    def __init__(self, schema: Dict):
        self.schema = schema

    def validate(self, scope: Dict) -> bool:
        if 'name' not in scope or 'description' not in scope:
            return False
        if not isinstance(scope['name'], str) or not isinstance(scope['description'], str):
            return False
        return True

    def check_pr(self, pr_scope: Dict) -> str:
        if self.validate(pr_scope):
            return 'scope-ok'
        else:
            return 'Validation failed: scope does not match schema'

class GitHubApp:
    def __init__(self, name: str):
        self.name = name

    def install(self, repository: str):
        print(f'Installing {self.name} on {repository}')

    def run_action(self, pr_scope: Dict) -> str:
        scope_shield = ScopeShield({'name': 'string', 'description': 'string'})
        return scope_shield.check_pr(pr_scope)

class GitHubAction:
    def __init__(self, app: GitHubApp):
        self.app = app

    def validate_pr(self, pr_scope: Dict) -> str:
        return self.app.run_action(pr_scope)
