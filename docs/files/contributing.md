# Contributing to NetCenLib

We warmly welcome contributions to the NetCenLib! This document provides guidelines for contributing to this project. By participating in this project, you agree to abide by its terms.

## Table of Content
- [How to contribute](#how-to-contribute)
- [Local development setup](#local-development-setup)
- [Release a version](#releasing-a-new-version)
- [Pre-commit hook](#precommit-hooks)

## How to Contribute

### Reporting Bugs and Requesting Features

- **Bug Reports**: Please use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md) to report any bugs. Provide as much detail as possible to help us understand and fix the issue.
- **Feature Requests**: For proposing new features or enhancements, use the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md). Describe the feature, its benefits, and possible implementation if you have one in mind.

### Making Changes

1. **Create an Issue**: For every change, whether a bug fix or a feature implementation, please open a new issue. This helps us keep track of what's being worked on and discuss potential changes before the development work starts.
2. **Follow the Style Guide**: Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) and other Python best practices to maintain code quality and readability.
3. **Write Tests**: Ensure that your changes have at least 80% test coverage. This helps maintain the library's reliability and ease future maintenance.
4. **Use Pre-commit**: This project uses pre-commit hooks to ensure code style and quality. Run `pre-commit install` after cloning the repository to set up the hooks locally. For more check [Pre-commit Hooks](#pre-commit-hooks).
5. **Pull Request**: Once you're ready, submit a pull request linked to the issue you've created. Describe your changes clearly in the PR description.


## Local development setup

By default venv is used to work on the project. After creating venv, install the requirements:

```bash
pip install -r requirements.txt
pip install -r requirements.dev.txt
```
and you are ready to go.

## Release a version

- Merge your PR into **`main`**
- Update changelog in CHANGELOG.md
- Change the version in src/netcenlib/version.py
- Commit. `git commit -m 'Release version x.y.z'`
- Tag the commit. `git tag -a x.y.z -m 'Release version x.y.z'`
- Push (do not forget --tags). `git push origin master --tags`
- Release will be created automatically by GitHub Actions


## Pre-commit Hooks

This project supports [**pre-commit**](https://pre-commit.com/). To use it please install it
in the `pip install pre-commit` and then run `pre-commit install` and you are ready to go.
Bunch of checks will be executed before commit and files will be formatted correctly.

Pre-commit works on staged files while commiting. To run it without a command one should run `pre-commit run`. Changes has to be staged.

To run pre-commit hooks on all changes in the branch:

1.  Sync branch with main
1.  Run `git diff --name-only --diff-filter=MA origin/master | xargs pre-commit run --files`

For branches that are not based on `master` you might replace `origin/master` with `origin/{your_branch}`
