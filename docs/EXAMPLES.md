# Advanced Examples

Practical examples for common Omni CLI use cases.

## Table of Contents

- [Memory Optimization Workflow](#memory-optimization-workflow)
- [MCP Server Management](#mcp-server-management)
- [Hostinger Infrastructure Automation](#hostinger-infrastructure-automation)
- [GitHub Repository Operations](#github-repository-operations)
- [Unleash Feature Flag Workflow](#unleash-feature-flag-workflow)
- [Combining Commands](#combining-commands)

## Memory Optimization Workflow

### Complete setup for a development Mac

```bash
# 1. Check current memory pressure
omni memory status

# 2. Connect and configure Thunderbolt 4 SSD
omni memory setup --disk /Volumes/ThunderboltSSD

# 3. Move heavy development caches
omni memory cache-move docker
omni memory cache-move gradle
omni memory cache-move npm

# 4. Start monitoring
omni memory monitor
```

### Automate cache relocation in your shell profile

Add to `~/.zshrc` or `~/.bashrc`:

```bash
# Omni CLI: Thunderbolt SSD caches
export GRADLE_USER_HOME=/Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/gradle
export NPM_CONFIG_CACHE=/Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/npm-cache
```

## MCP Server Management

### Add common MCP servers

```bash
# File system access
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)

# SQLite database
omni mcp add sqlite npx -y @modelcontextprotocol/server-sqlite /path/to/database.db

# GitHub MCP server
omni mcp add github npx -y @modelcontextprotocol/server-github

# Test all servers
omni mcp test filesystem
omni mcp test sqlite
omni mcp test github
```

### Backup MCP configuration

```bash
cp ~/.config/mcp/servers.json ~/.config/mcp/servers.json.backup
```

## Hostinger Infrastructure Automation

### Complete domain + VPS setup

```bash
# List your resources
omni hostinger domains
omni hostinger vps

# Check DNS records
omni hostinger dns conecthu.com

# (Use Hostinger API or dashboard to update records as needed)
```

### Find VPS IP for SSH

```bash
omni hostinger vps | grep "your-vps-hostname"
```

## GitHub Repository Operations

### Daily workflow

```bash
# Check your latest repositories
omni github repos --user mateussiqueira

# Find trending Python projects
omni github trending --lang python

# Clone a useful project
omni github clone owner/project-name --dir ./local-folder
```

### Batch clone from a list

```bash
for repo in "mateussiqueira/omni-cli" "mateussiqueira/unleash" "mateussiqueira/easy-mcp-br"; do
    omni github clone "$repo" --dir "./$(basename $repo)"
done
```

## Unleash Feature Flag Workflow

### Release process with feature flags

```bash
# Create feature flag for new feature
omni unleash create new-checkout-flow --desc "New checkout flow for mobile"

# Enable in development project
omni unleash toggle new-checkout-flow true --project dev

# Later, enable in production
omni unleash toggle new-checkout-flow true --project production

# List all flags
omni unleash flags --project production
```

### Sunset a feature

```bash
# Disable flag
omni unleash toggle legacy-auth false

# (Remove flag from code and Unleash dashboard when safe)
```

## Combining Commands

### Check everything at once

```bash
#!/bin/bash
# daily-check.sh

echo "=== Omni CLI Daily Check ==="
echo ""
echo "Memory:"
omni memory status

echo ""
echo "MCP Servers:"
omni mcp list

echo ""
echo "Hostinger Domains:"
omni hostinger domains

echo ""
echo "GitHub Repos:"
omni github repos
```

### Environment setup script

```bash
#!/bin/bash
# setup-dev-env.sh

# Configure Omni CLI from environment variables
omni config set hostinger_api_token "$HOSTINGER_TOKEN"
omni config set github_token "$GITHUB_TOKEN"
omni config set github_username "$GITHUB_USER"
omni config set thunderbolt_disk "/Volumes/ThunderboltSSD"

echo "✅ Development environment configured"
```

## Tips and Tricks

### Alias for common commands

Add to your shell profile:

```bash
alias omni-mem='omni memory status'
alias omni-repos='omni github repos --user mateussiqueira'
alias omni-flags='omni unleash flags --project default'
```

### Cron job for memory monitoring

```bash
# Check memory every hour and log it
0 * * * * /usr/local/bin/omni memory status >> /var/log/omni-memory.log 2>&1
```

## Next Steps

- Read the [Getting Started Guide](GETTING_STARTED.md)
- Check the [Command Reference](COMMANDS.md)
- See [Troubleshooting](TROUBLESHOOTING.md) if you encounter issues
