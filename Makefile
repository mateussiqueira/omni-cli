.PHONY: install install-dev test lint format type-check clean build release help shell-completion

PYTHON := python3
VENV := .venv
VENV_BIN := $(VENV)/bin

help:
	@echo "Available commands:"
	@echo "  make install      - Install package"
	@echo "  make install-dev  - Install package with dev dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters (ruff)"
	@echo "  make format       - Format code (black)"
	@echo "  make type-check   - Run type checker (mypy)"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make build        - Build package for distribution"
	@echo "  make release      - Build and check package"
	@echo "  make shell-completion - Install shell completion"

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(VENV_BIN)/pip install --upgrade pip

install: $(VENV)
	$(VENV_BIN)/pip install -e .

install-dev: $(VENV)
	$(VENV_BIN)/pip install -e ".[dev]"

test:
	$(VENV_BIN)/pytest

lint:
	$(VENV_BIN)/ruff check src/omni tests
	$(VENV_BIN)/black --check src/omni tests

format:
	$(VENV_BIN)/black src/omni tests
	$(VENV_BIN)/ruff check --fix src/omni tests

type-check:
	$(VENV_BIN)/mypy src/omni

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	$(PYTHON) -m build

release: build
	$(VENV_BIN)/twine check dist/*

shell-completion:
	@echo "Installing shell completions..."
	$(VENV_BIN)/omni --install-completion bash || true
	$(VENV_BIN)/omni --install-completion zsh || true
	$(VENV_BIN)/omni --install-completion fish || true
	@echo "✅ Shell completion installed. Restart your terminal."
