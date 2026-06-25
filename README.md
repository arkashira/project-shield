# Project Shield
A GitHub App that validates pull requests against a defined scope.

## Installation
To install the app, simply run `poetry install` and then `poetry run python -m pytest` to run the tests.

## Usage
To use the app, create a new instance of the `GitHubApp` class and call the `install` method to install it on a repository. Then, create a new instance of the `GitHubAction` class and call the `validate_pr` method to validate a pull request.
