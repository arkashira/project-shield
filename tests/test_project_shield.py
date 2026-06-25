from project_shield import ScopeShield, GitHubApp, GitHubAction
import pytest

def test_scope_shield_validate():
    scope_shield = ScopeShield({'name': 'string', 'description': 'string'})
    scope = {'name': 'test', 'description': 'test description'}
    assert scope_shield.validate(scope) == True

def test_scope_shield_validate_invalid():
    scope_shield = ScopeShield({'name': 'string', 'description': 'string'})
    scope = {'name': 123, 'description': 'test description'}
    assert scope_shield.validate(scope) == False

def test_scope_shield_check_pr():
    scope_shield = ScopeShield({'name': 'string', 'description': 'string'})
    scope = {'name': 'test', 'description': 'test description'}
    assert scope_shield.check_pr(scope) == 'scope-ok'

def test_scope_shield_check_pr_invalid():
    scope_shield = ScopeShield({'name': 'string', 'description': 'string'})
    scope = {'name': 123, 'description': 'test description'}
    assert scope_shield.check_pr(scope) == 'Validation failed: scope does not match schema'

def test_github_app_install():
    app = GitHubApp('ScopeShield')
    app.install('test-repo')
    # No assertion, just testing that it runs without error

def test_github_app_run_action():
    app = GitHubApp('ScopeShield')
    scope = {'name': 'test', 'description': 'test description'}
    assert app.run_action(scope) == 'scope-ok'

def test_github_action_validate_pr():
    app = GitHubApp('ScopeShield')
    action = GitHubAction(app)
    scope = {'name': 'test', 'description': 'test description'}
    assert action.validate_pr(scope) == 'scope-ok'
