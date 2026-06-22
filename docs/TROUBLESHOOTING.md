# Troubleshooting

Common issues and solutions when using Omni CLI.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Permission Issues](#permission-issues)
- [Memory Commands](#memory-commands)
- [Hostinger API](#hostinger-api)
- [GitHub API](#github-api)
- [MCP Servers](#mcp-servers)
- [Shell Completion](#shell-completion)
- [Getting Help](#getting-help)

## Installation Issues

### `pip install omni-cli` fails with "externally-managed-environment"

**Cause**: Modern Python distributions prevent installing packages system-wide.

**Solutions**:

```bash
# Option 1: Use a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install omni-cli

# Option 2: Use pipx
pip install pipx
pipx install omni-cli
```

### Command not found after installation

**Cause**: The Python scripts directory is not in your PATH.

**Solutions**:

```bash
# macOS/Linux - add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Or with pipx
pipx ensurepath
```

Restart your terminal after making changes.

## Permission Issues

### `omni memory setup` requires sudo

**Cause**: Setting up swap and system-wide LaunchAgents requires root privileges.

**Solution**:

```bash
sudo omni memory setup --disk /Volumes/ThunderboltSSD
```

### Cannot write to Thunderbolt SSD

**Cause**: The disk may be formatted as read-only or owned by another user.

**Solution**:

```bash
# Check disk permissions
ls -ld /Volumes/ThunderboltSSD

# Fix permissions (if needed)
sudo chown -R $(whoami) /Volumes/ThunderboltSSD
```

## Memory Commands

### `omni memory status` shows "Thunderbolt SSD: Not connected"

**Cause**: The configured disk path does not exist.

**Solution**:

```bash
# Check available disks
ls /Volumes/

# Update the path
omni config set thunderbolt_disk /Volumes/YourDiskName
```

### Swap file creation fails

**Cause**: macOS manages swap automatically; manual swap files are limited.

**Solution**: Let macOS handle swap automatically. Use the Thunderbolt SSD for app caches instead:

```bash
omni memory cache-move docker
omni memory cache-move gradle
```

## Hostinger API

### `omni hostinger domains` returns authentication error

**Cause**: The Hostinger API token is missing or invalid.

**Solution**:

```bash
export OMNI_HOSTINGER_API_TOKEN=your_token_here
# Or
omni config set hostinger_api_token your_token_here
```

### API rate limit exceeded

**Cause**: Too many requests in a short time.

**Solution**: Wait a few minutes before retrying. Avoid running commands in tight loops.

## GitHub API

### `omni github repos` shows 401 or 403 error

**Cause**: The GitHub token is missing, expired, or lacks permissions.

**Solution**:

1. Create a token at https://github.com/settings/tokens
2. Set it:

```bash
export OMNI_GITHUB_TOKEN=your_token_here
export OMNI_GITHUB_USERNAME=your_username
```

### Private repositories not showing

**Cause**: The token does not have `repo` scope.

**Solution**: Regenerate your GitHub token with `repo` scope enabled.

## MCP Servers

### `omni mcp test` fails immediately

**Cause**: The MCP server command is not installed or not in PATH.

**Solution**:

```bash
# Verify the command exists
which npx
which docker

# Install if missing
npm install -g npx
```

### MCP config file is not found

**Cause**: The default path does not exist.

**Solution**:

```bash
# Set a custom path
omni config set mcp_config_path ~/.config/mcp/servers.json

# Or create the default directory
mkdir -p ~/.config/mcp
```

## Shell Completion

### Completion does not work after installation

**Cause**: The shell configuration file was not reloaded.

**Solution**:

```bash
# Bash
source ~/.bashrc

# Zsh
source ~/.zshrc
```

### `omni completion install zsh` fails

**Cause**: The Zsh site-functions directory does not exist or requires sudo.

**Solution**:

```bash
# Create the directory
sudo mkdir -p /usr/local/share/zsh/site-functions

# Then install
omni completion install zsh
```

## Getting Help

If your issue is not listed here:

1. Check the [FAQ](FAQ.md)
2. Read the [Command Reference](COMMANDS.md)
3. Open an issue on GitHub: https://github.com/mateussiqueira/omni-cli/issues

When reporting issues, include:
- Omni CLI version (`omni --version`)
- Python version (`python --version`)
- Operating system
- Full error message
- Steps to reproduce
