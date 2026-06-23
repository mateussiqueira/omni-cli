# Omni CLI

**The CLI of CLIs** — A unified hub to orchestrate development tools.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/mateussiqueira/omni-cli/blob/main/LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-omni--cli-blue)](https://pypi.org/project/omni-cli/)
[![CI](https://github.com/mateussiqueira/omni-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/mateussiqueira/omni-cli/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://mateussiqueira.github.io/omni-cli/)

---

## What is Omni CLI?

Omni CLI is a **unified command-line interface** that connects and orchestrates multiple development tools in a single, consistent interface. Instead of remembering different CLI syntax for each tool, you use one CLI to rule them all.

```text
  ██████  ███    ███ ██ ███    ██
 ██    ██ ████  ████ ██ ████   ██
 ██    ██ ██ ████ ██ ██ ██ ██  ██
 ██    ██ ██  ██  ██ ██ ██  ██ ██
  ██████  ██      ██ ██ ██   ████
```

---

## Features

### 🤖 AI & MCP
Manage MCP (Model Context Protocol) servers for AI tool integration — add, remove, test, and monitor your AI agent infrastructure.

### 🧠 Memory Optimization
Optimize macOS memory using Thunderbolt 4 SSD as swap and cache extension. Monitor memory pressure, move app caches, and configure automatic optimization.

### 🌐 Cloud Management
- **Hostinger** — Domains, DNS zones, and VPS management
- **Cloudflare** — DNS records and cache purging
- **AWS** — S3, EC2, and Route53 operations
- **Vercel** — Project and deployment management

### 🐙 GitHub
Repository management, trending repositories, and batch cloning — all from the command line.

### 🚦 Feature Flags
Manage Unleash feature flags: toggle, create, archive, and check flag status across environments.

### 🔌 Plugin System
Extend Omni CLI with external plugins discovered via Python entry points. Install, list, and remove plugins dynamically.

### 🎭 Profiles
Switch between development, staging, and production configurations with a single command. Isolated credentials per profile.

### ⚙️ Smart Configuration
Centralized config via TOML files and environment variables. Single source of truth for all tools.

---

## Quick Start

### Install

```bash
pip install omni-cli
```

Or from source:

```bash
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli
pip install -e ".[dev]"
```

### Verify

```bash
omni version
# Omni CLI version 0.1.0
```

### Explore

```bash
omni status            # System status
omni --help            # All commands
omni memory status     # Memory status
omni github trending   # GitHub trending repos
```

---

## Command Groups

| Command | Description |
|---------|-------------|
| `omni memory` | 🧠 Mac memory optimization |
| `omni mcp` | 🔌 MCP server management |
| `omni hostinger` | 🌐 Hostinger domain/VPS management |
| `omni cloudflare` | ☁️ Cloudflare management |
| `omni aws` | 🌩️ AWS management |
| `omni vercel` | ▲ Vercel management |
| `omni github` | 🐙 GitHub repository management |
| `omni unleash` | 🚦 Unleash feature flags |
| `omni plugins` | 🔌 Plugin management |
| `omni config` | ⚙️ Configuration management |
| `omni completion` | 🐚 Shell completion |
| `omni update` | 🚀 Self-update |

---

## Documentation

- **[Getting Started](GETTING_STARTED.md)** — First steps with Omni CLI
- **[Installation](INSTALLATION.md)** — Detailed installation guide
- **[Command Reference](COMMANDS.md)** — Complete command reference
- **[Examples](EXAMPLES.md)** — Practical usage examples
- **[Architecture](ARCHITECTURE.md)** — Project architecture
- **[Use Cases](USE_CASES.md)** — Real-world scenarios
- **[FAQ](FAQ.md)** — Frequently asked questions
- **[Troubleshooting](TROUBLESHOOTING.md)** — Common issues

### Advanced Topics

- **[Memory Deep Dive](MEMORY_DEEP_DIVE.md)** — macOS memory internals
- **[MCP Integration](MCP_INTEGRATION.md)** — AI tool integration
- **[Plugin Development](PLUGIN_DEVELOPMENT.md)** — Create plugins
- **[Enterprise Setup](ENTERPRISE_SETUP.md)** — Team/org deployment
- **[Performance](PERFORMANCE.md)** — Optimization tips
- **[Migration](MIGRATION.md)** — Migrating from other tools

---

## Project Structure

```text
omni-cli/
├── src/omni/
│   ├── cli.py              # Main entrypoint
│   ├── commands/           # 12 command modules
│   │   ├── memory.py       # Memory optimization
│   │   ├── mcp.py          # MCP servers
│   │   ├── hostinger.py    # Hostinger API
│   │   ├── cloudflare.py   # Cloudflare API
│   │   ├── aws.py         # AWS operations
│   │   ├── vercel.py       # Vercel management
│   │   ├── github.py       # GitHub API
│   │   ├── unleash.py      # Feature flags
│   │   ├── plugins.py      # Plugin system
│   │   ├── config.py       # Configuration
│   │   ├── completion.py   # Shell completion
│   │   └── update.py       # Self-update
│   └── core/               # Core framework
│       ├── config.py       # Pydantic config
│       ├── executor.py     # Shell executor
│       ├── logger.py       # Logging + audit
│       ├── plugins.py      # Plugin discovery
│       └── profiles.py     # Profile management
├── tests/                  # Test suite
├── docs/                   # Documentation
├── assets/                 # Logos and images
└── pyproject.toml          # Project config
```

---

## License

MIT &copy; [Mateus Siqueira](https://github.com/mateussiqueira)
