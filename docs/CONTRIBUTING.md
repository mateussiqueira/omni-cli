# Contributing to Omni CLI

Thank you for your interest in contributing to Omni CLI! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:

- A clear title and description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Omni CLI version (`omni --version`)
- Python version and operating system

### Suggesting Features

Feature suggestions are welcome! Please open an issue and describe:

- The problem you're trying to solve
- Your proposed solution
- Any alternatives you've considered

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting:

```bash
make test
make lint
make type-check
```

5. Commit your changes with clear messages
6. Push to your fork
7. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Code Style

We use:
- **Black** for code formatting
- **Ruff** for linting
- **MyPy** for type checking

Run before committing:

```bash
make format
make lint
make type-check
```

## Testing

All new features should include tests. Run the test suite with:

```bash
make test
```

## Documentation

When adding new commands or features, please update:

- The relevant command file in `src/omni/commands/`
- `docs/COMMANDS.md` and `docs/COMMANDS.pt.md`
- `README.md` and `README.pt.md` if needed
- This guide if contributing processes change

## Commit Messages

Use clear and descriptive commit messages:

```text
Add feature X to command Y

- Detailed explanation
- Another relevant detail
```

## Code of Conduct

Please be respectful and constructive in all interactions. See [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md).

## Questions?

Feel free to open an issue for discussion.
