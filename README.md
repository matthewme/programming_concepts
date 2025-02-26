# Programming Concepts

TODO: Add project description

---

## Table of Contents

- [Requirements](#requirements)
- [Features](#features)
- [Development Environment](#development-environment)
- [Development Workflow](#development-workflow)
- [Dependency Management](#dependency-management)

---

## Requirements

- `pyenv`

  ```bash
  brew install pyenv
  ```

  Add the following to your `.zshrc` file

  ```bash
  # Initialize pyenv
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  ```

- `pyenv-virtualenv`

  ```bash
  brew install pyenv-virtualenv
  ```

  Add the following to your `.zshrc` file

  ```bash
  # Initialize pyenv-virtualenv
  eval "$(pyenv virtualenv-init -)"
  ```

- Node.js (for `pyright`)

---

## Features

- **Type Safety**: Python 3.12 type annotations checked with `pyright`.
- **Testing**: Comprehensive unit tests using `pytest`.
- **Code Quality**: Linting with `flake8` and formatting with `black`.
- **Environment Management**: Virtual environments with `pyenv`.

---

## Development Environment

### Setting Up Your Development Environment

Follow these steps to configure your development environment for the project:

### Python Environment

1. Install Python 3.12 using `pyenv`:

   ```bash
   pyenv install 3.12.0
   ```

1. Create a virtual environment for the project:

   ```bash
   pyenv virtualenv 3.12.0 prog-concepts-env
   ```

1. Set the virtual environment as the default for the project directory:

   ```bash
   pyenv local prog-concepts-env
   ```

   This will create a `.python-version` file in your project directory,
   ensuring the correct Python version and virtual environment are
   automatically activated when you navigate into the project folder.

1. Activate the virtual environment:

   ```bash
   pyenv activate prog-concepts-env
   ```

1. Install all project dependencies (including development tools):

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   If you have problems with pip certificates, run this command

   ```bash
   pip config set global.trusted-host \
       "pypi.org files.pythonhosted.org pypi.python.org" \
       --trusted-host=pypi.python.org \
       --trusted-host=pypi.org \
       --trusted-host=files.pythonhosted.org
   ```

1. Install pre-commit hooks

   This project uses Pre-Commit to automatically run quality checks every time
   you make a `git commit`. This helps catch issues early and ensures that the
   codebase maintains consistent quality.

   When configured correctly, Pre-Commit hooks will:

   - Automatically run tools such as Black, Flake8, Pyright, and Pytest on your
     staged changes.
   - Prevent commits if any issues are found.

   If your local development environment is not configured correctly, these
   checks will not run, and errors may only be detected later in the CI
   pipeline. To avoid delays, ensure Pre-Commit is set up before contributing.

   ```bash
   pre-commit install
   ```

1. Install `pyright`:

   Since `Pyright` is a Node.js-based tool, install it globally using `npm`:

   ```bash
       npm install -g pyright
   ```

---

### Included Development Tools

The following development tools are installed automatically from `requirements.txt`:

- **Code Formatting**: `black`
- **Linting**: `flake8`
- **Testing**: `pytest` and `pytest-cov`
- **Static Type Checking**: `pyright` and `mypy`

---

### Editor Configuration

#### VS Code

1. Install the following extensions:

   - Python (by Microsoft)
   - Pylance (for Pyright integration)
   - Black Formatter

2. Add these settings to your `settings.json` file:

```json
{
  "python.pythonPath": "~/.pyenv/versions/validator-env/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "editor.formatOnSave": true,
  "python.analysis.typeCheckingMode": "strict"
}
```

---

## Development Workflow

### Run all Linting and Testing

Run all including quality checks.

```bash
./dev_validate.sh
```

### Pre-Commit Hooks

This project uses Pre-Commit to automatically run quality checks on each `git
commit`. If you don’t see output from Black, Flake8, Pyright, and Pytest during
a commit, check the Development Environment section for setup instructions.

### Test Watch Mode

Run tests in watch mode (tests will auto-run on every file change).

```bash
ptw
```

### Code Formatting

Format the codebase using `black`:

```bash
black src/ tests/
```

### Linting

Run `flake8` to check for linting errors:

```bash
flake8 src/
```

### Static Type Checking

Run `pyright` to ensure type correctness:

```bash
pyright
```

### Testing

Use `pytest` to execute unit tests:

```bash
pytest
```

By default, only the faster unit tests are run. Slower tests, such as
end-to-end (E2E) tests, are excluded. To include these slower tests in your
test run, use the following command:

```bash
pytest -m slow
```

To mark a test as slow, use the `@pytest.mark.slow` decorator in your test
file. This allows you to selectively include or exclude slow tests during test
execution.

Example:

```python
from pytest import mark

@mark.slow
def test_e2e_slow_running():
    """Test a slow running e2e process"""
    # test implementation here
```

---

## Dependency Management

This project uses a `requirements.txt` file to define both runtime and
development dependencies.

---

### Installing Dependencies

1. **Activate the Virtual Environment**:
   Ensure your virtual environment is active before installing dependencies:

   ```bash
   pyenv activate validator-env
   ```

1. **Install All Dependencies**:
   Use `pip` to install all packages defined in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

1. **Install Project Package**:
   Use `pip` to install the project package in editable mode. This allows the
   virtual environment to automatically detect and apply updates to the package
   as you make changes to the source code:

   ```bash
   pip install -e .
   ```

---

### Adding New Dependencies

1. **Install the Package**:
   Use `pip` to install a new dependency:

   ```bash
    pip install package_name
   ```

2. **Update `requirements.txt`**:
   After installing a new package, update the `requirements.txt` file:

   ```bash
    pip freeze > requirements.txt
   ```

3. **Commit Changes**:
   Add the updated `requirements.txt` file to version control:

   ```bash
    git add requirements.txt
    git commit -m "Add package_name to dependencies"
   ```

---

### Checking for Dependency Updates

1. **Check for Outdated Packages**:
   List all outdated packages:

   ```bash
   pip list --outdated
   ```

2. **Update Specific Packages**:
   To update a specific package, run:

   ```bash
   pip install --upgrade package_name
   ```

3. **Regenerate `requirements.txt`**:
   After updating, regenerate the `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

