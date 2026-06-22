import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Commit:
    timestamp: str
    message: str

class ProjectShield:
    def __init__(self, scope_document: str, commits: List[Commit]):
        self.scope_document = scope_document
        self.commits = commits

    def get_scope_document(self) -> str:
        return self.scope_document

    def get_commits(self) -> List[Commit]:
        return self.commits

    def get_latest_version(self) -> str:
        if not self.commits:
            return "No commits"
        return self.commits[-1].message

    def get_commit_history(self) -> List[dict]:
        return [{"timestamp": commit.timestamp, "message": commit.message} for commit in self.commits]
