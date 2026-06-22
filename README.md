# 🌟 Omni CLI

> **The CLI of CLIs** — A unified hub to orchestrate development tools.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-4%2F4%20passing-brightgreen)](tests)

```text
  ██████  ███    ███ ██ ███    ██
 ██    ██ ████  ████ ██ ████   ██
 ██    ██ ██ ████ ██ ██ ██ ██  ██
 ██    ██ ██  ██  ██ ██ ██  ██ ██
  ██████  ██      ██ ██ ██   ████
```

## 🚀 Overview

**Omni CLI** is a unified command-line hub that connects and orchestrates multiple development tools in a single interface:

- 🧠 **Memory**: macOS memory optimization using Thunderbolt 4 SSD
- 🔌 **MCP**: Model Context Protocol server management
- 🌐 **Hostinger**: Domain, DNS, and VPS management
- 🐙 **GitHub**: Repository management, trending, and cloning
- 🚦 **Unleash**: Feature flag management
- ⚙️ **Config**: Centralized configuration

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Or install directly
pip install .
```

## ⚡ Quick Start

```bash
# Show overall status
omni status

# Show version
omni version

# Interactive initial setup
omni config init
```

## 📚 Documentation

- [Getting Started](docs/GETTING_STARTED.md)
- [Command Reference](docs/COMMANDS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Português](README.pt.md)

## 🧠 Memory Commands

Optimize your Mac using a Thunderbolt 4 SSD as memory extension:

```bash
# Check memory status
omni memory status

# Setup Thunderbolt SSD
omni memory setup --disk /Volumes/ThunderboltSSD

# Start monitoring
omni memory monitor

# Move heavy app caches
omni memory cache-move docker
```

## 🔌 MCP Commands

Manage MCP servers:

```bash
# List servers
omni mcp list

# Add a server
omni mcp add my-server npx -y @modelcontextprotocol/server-filesystem /path

# Remove a server
omni mcp remove my-server

# Test a server
omni mcp test my-server
```

## 🌐 Hostinger Commands

Manage your Hostinger infrastructure:

```bash
# List domains
omni hostinger domains

# List VPS instances
omni hostinger vps

# Show DNS records
omni hostinger dns conecthu.com
```

Set the token:

```bash
export OMNI_HOSTINGER_API_TOKEN=your_token_here
```

## 🐙 GitHub Commands

```bash
# List repositories
omni github repos --user mateussiqueira

# Trending repositories
omni github trending --lang python

# Clone a repository
omni github clone mateussiqueira/omni-cli
```

Set credentials:

```bash
export OMNI_GITHUB_TOKEN=your_token_here
export OMNI_GITHUB_USERNAME=mateussiqueira
```

## 🚦 Unleash Commands

```bash
# List feature flags
omni unleash flags --project default

# Create a feature flag
omni unleash create my-flag --desc "Flag description"

# Enable/disable
omni unleash toggle my-flag true
omni unleash toggle my-flag false
```

Set credentials:

```bash
export OMNI_UNLEASH_URL=https://your-unleash.com
export OMNI_UNLEASH_API_TOKEN=your_token
```

## ⚙️ Configuration

Omni CLI stores settings in `~/.config/omni/config.toml`.

```bash
# Interactive setup
omni config init

# Show configuration
omni config show

# Set a value
omni config set thunderbolt_disk /Volumes/MySSD

# Show environment variables
omni config env
```

## 🧪 Testing

```bash
pytest
```

## 🏗️ Architecture

```text
omni-cli/
├── src/omni/
│   ├── cli.py              # Main entrypoint
│   ├── commands/           # Domain-specific commands
│   │   ├── memory.py
│   │   ├── mcp.py
│   │   ├── hostinger.py
│   │   ├── github.py
│   │   ├── unleash.py
│   │   └── config.py
│   └── core/               # Core utilities
│       ├── config.py
│       └── executor.py
├── tests/                  # Tests
├── docs/                   # Documentation (EN & PT)
└── pyproject.toml          # Project configuration
```

## 🌍 Leading Open Source Countries

| Rank | Country | Highlight |
|------|---------|-----------|
| 1 | 🇺🇸 USA | Largest number of projects and contributors |
| 2 | 🇨🇳 China | Large developer base (GitHub, Gitee) |
| 3 | 🇩🇪 Germany | Technical quality, Linux, KDE |
| 4 | 🇬🇧 UK | Innovation in web and infrastructure |
| 5 | 🇮🇳 India | Fast-growing community |
| 6 | 🇫🇷 France | Important European projects |
| 7 | 🇨🇦 Canada | Strong presence in AI and open data |
| 8 | 🇧🇷 Brazil | Active community, Python, PHP, JS |
| 9 | 🇯🇵 Japan | Ruby, infrastructure |
| 10 | 🇷🇺 Russia | Systems and security projects |

## 🤝 Contributing

1. Fork the project
2. Create your branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with 💙 by [Mateus Siqueira](https://github.com/mateussiqueira)
