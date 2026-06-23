# Getting Started

Welcome to **Omni CLI** — the CLI of CLIs.

## Prerequisites

- Python 3.10 or higher
- macOS, Linux, or Windows
- (Optional) GitHub CLI (`gh`) for repository operations

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Omni CLI

```bash
pip install -e ".[dev]"
```

## First Steps

### 1. Check the installation

```bash
omni version
```

Expected output:

```text
Omni CLI version 0.1.0
```

### 2. Run the status command

```bash
omni status
```

### 3. Configure credentials

```bash
omni config init
```

This interactive command will ask for:
- Hostinger API token
- GitHub token and username
- Unleash URL and token
- Thunderbolt SSD path

You can also set values via environment variables:

```bash
export OMNI_HOSTINGER_API_TOKEN=your_token
export OMNI_GITHUB_TOKEN=your_token
export OMNI_GITHUB_USERNAME=your_username
export OMNI_UNLEASH_URL=https://your-unleash.com
export OMNI_UNLEASH_API_TOKEN=your_token
export OMNI_THUNDERBOLT_DISK=/Volumes/ThunderboltSSD
```

## Quick Examples

### Memory optimization

```bash
omni memory status
omni memory setup --disk /Volumes/ThunderboltSSD
```

### Hostinger management

```bash
omni hostinger domains
omni hostinger vps
omni hostinger dns conecthu.com
```

### Cloudflare, AWS, Vercel

```bash
omni cloudflare zones
omni aws status
omni vercel projects
```

### GitHub operations

```bash
omni github repos --user mateussiqueira
omni github clone mateussiqueira/omni-cli
```

### MCP management

```bash
omni mcp list
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users
```

### Plugins and profiles

```bash
omni plugins list
omni config profile create production
omni config profile use production
```

## Next Steps

- Read the [Command Reference](COMMANDS.md)
- Learn about the [Architecture](ARCHITECTURE.md)
- Explore [Plugin Development](PLUGIN_DEVELOPMENT.md)
- Read in [Português](https://github.com/mateussiqueira/omni-cli/blob/main/README.pt.md)
