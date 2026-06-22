# Installation Guide

Complete guide to install Omni CLI on any platform.

## Table of Contents

- [System Requirements](#system-requirements)
- [Install from PyPI](#install-from-pypi)
- [Install from Source](#install-from-source)
- [Install with pipx](#install-with-pipx)
- [Install on macOS](#install-on-macos)
- [Install on Linux](#install-on-linux)
- [Install on Windows](#install-on-windows)
- [Verify Installation](#verify-installation)
- [Upgrade](#upgrade)
- [Uninstall](#uninstall)

## System Requirements

- **Python**: 3.10 or higher
- **Operating System**: macOS, Linux, or Windows
- **Disk Space**: ~50 MB minimum
- **RAM**: 512 MB minimum (for CLI operations)

## Install from PyPI

The easiest and recommended way to install Omni CLI:

```bash
pip install omni-cli
```

To install with development dependencies:

```bash
pip install "omni-cli[dev]"
```

### Using pipx (Recommended for CLI Tools)

[pipx](https://pypa.github.io/pipx/) installs Python CLI tools in isolated environments:

```bash
# Install pipx if you don't have it
pip install pipx
pipx ensurepath

# Install Omni CLI
pipx install omni-cli
```

## Install from Source

For development or to get the latest unreleased features:

```bash
# Clone the repository
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli

# Create a virtual environment
python3 -m venv .venv

# Activate the environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Install on macOS

### Using Homebrew (when available)

```bash
brew install omni-cli
```

### Using pip

```bash
python3 -m pip install omni-cli
```

### For Apple Silicon (M1/M2/M3)

Omni CLI works natively on Apple Silicon. If you encounter architecture issues, ensure you are using the arm64 version of Python:

```bash
python3 -c "import platform; print(platform.machine())"
# Should output: arm64
```

## Install on Linux

### Using pip

```bash
python3 -m pip install omni-cli
```

### Using your distribution's package manager (when available)

```bash
# Ubuntu/Debian (when .deb is available)
sudo dpkg -i omni-cli_0.1.0_amd64.deb

# Fedora/RHEL (when .rpm is available)
sudo rpm -i omni-cli-0.1.0.x86_64.rpm
```

## Install on Windows

### Using pip

```powershell
python -m pip install omni-cli
```

### Using pipx

```powershell
pip install pipx
pipx ensurepath
pipx install omni-cli
```

After installation, you may need to restart your terminal or PowerShell session.

## Verify Installation

Run the following commands to verify the installation:

```bash
# Check version
omni --version

# Check status
omni status

# Show help
omni --help
```

Expected output for version:

```text
Omni CLI 0.1.0
```

## Upgrade

To upgrade to the latest version:

```bash
pip install --upgrade omni-cli
```

Or with pipx:

```bash
pipx upgrade omni-cli
```

## Uninstall

To remove Omni CLI:

```bash
pip uninstall omni-cli
```

Or with pipx:

```bash
pipx uninstall omni-cli
```

## Post-Installation

After installing, run the interactive configuration:

```bash
omni config init
```

This will guide you through setting up:
- Hostinger API token
- GitHub token and username
- Unleash URL and token
- Thunderbolt SSD path
- MCP config path

## Next Steps

- Read the [Getting Started Guide](GETTING_STARTED.md)
- Explore the [Command Reference](COMMANDS.md)
- Check the [FAQ](FAQ.md) for common questions
