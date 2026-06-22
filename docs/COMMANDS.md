# Command Reference

Complete reference for Omni CLI commands.

## Global Options

```bash
omni --version     # Show version
omni --help        # Show help
```

## `omni memory`

Memory optimization commands for macOS using Thunderbolt 4 SSD.

| Command | Description |
|---------|-------------|
| `omni memory status` | Show current memory and swap status |
| `omni memory setup` | Configure Thunderbolt SSD as memory extension |
| `omni memory monitor` | Start memory monitoring daemon |
| `omni memory cache-move <app>` | Move app cache to Thunderbolt SSD |

### Examples

```bash
# Show memory status
omni memory status

# Setup with custom disk
omni memory setup --disk /Volumes/MySSD

# Move Docker cache
omni memory cache-move docker
```

## `omni mcp`

Model Context Protocol server management.

| Command | Description |
|---------|-------------|
| `omni mcp list` | List configured MCP servers |
| `omni mcp add <name> <command> [args...]` | Add MCP server |
| `omni mcp remove <name>` | Remove MCP server |
| `omni mcp test <name>` | Test MCP server |

### Examples

```bash
omni mcp list
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users
omni mcp test filesystem
omni mcp remove filesystem
```

## `omni hostinger`

Hostinger infrastructure management.

| Command | Description |
|---------|-------------|
| `omni hostinger domains` | List domains |
| `omni hostinger vps` | List VPS instances |
| `omni hostinger dns <domain>` | Show DNS records |

### Environment

```bash
export OMNI_HOSTINGER_API_TOKEN=your_token
```

## `omni github`

GitHub operations.

| Command | Description |
|---------|-------------|
| `omni github repos [--user <user>]` | List repositories |
| `omni github trending [--lang <lang>]` | Show trending repositories |
| `omni github clone <repo> [--dir <dir>]` | Clone a repository |

### Environment

```bash
export OMNI_GITHUB_TOKEN=your_token
export OMNI_GITHUB_USERNAME=your_username
```

## `omni unleash`

Unleash feature flag management.

| Command | Description |
|---------|-------------|
| `omni unleash flags [--project <id>]` | List feature flags |
| `omni unleash create <name> [--desc <desc>]` | Create feature flag |
| `omni unleash toggle <name> <true|false>` | Toggle feature flag |

### Environment

```bash
export OMNI_UNLEASH_URL=https://your-unleash.com
export OMNI_UNLEASH_API_TOKEN=your_token
```

## `omni config`

Configuration management.

| Command | Description |
|---------|-------------|
| `omni config show` | Show current configuration |
| `omni config set <key> <value>` | Set configuration value |
| `omni config env` | Show environment variables |
| `omni config init` | Interactive initial setup |

### Examples

```bash
omni config init
omni config show
omni config set thunderbolt_disk /Volumes/ThunderboltSSD
```

## `omni completion`

Shell completion setup.

| Command | Description |
|---------|-------------|
| `omni completion bash` | Show Bash completion instructions |
| `omni completion zsh` | Show Zsh completion instructions |
| `omni completion install <bash\|zsh>` | Install completion automatically |

### Examples

```bash
omni completion install bash
omni completion install zsh
omni completion bash
```

## `omni status`

Show overall Omni CLI status.

## `omni version`

Show Omni CLI version.
