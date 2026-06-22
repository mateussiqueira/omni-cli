# Frequently Asked Questions (FAQ)

## General

### What is Omni CLI?

Omni CLI is a unified command-line hub that connects multiple development tools (memory optimization, MCP, Hostinger, GitHub, Unleash) in a single interface.

### Is Omni CLI free?

Yes, Omni CLI is open source and free under the MIT License.

### Which platforms are supported?

macOS, Linux, and Windows with Python 3.10 or higher.

## Installation

### Can I install Omni CLI without sudo?

Yes, using a virtual environment or pipx is recommended and does not require sudo.

```bash
pipx install omni-cli
```

### Can I install multiple versions?

It's best to use virtual environments for different versions.

## Memory

### Does Omni CLI increase my physical RAM?

No. Omni CLI helps optimize memory usage by moving heavy caches to an external Thunderbolt 4 SSD and monitoring memory pressure.

### Will using an external SSD as swap damage it?

SSDs have finite write endurance. A high-quality Thunderbolt 4 SSD with DRAM cache and good endurance rating can handle swap operations well, but intensive swapping may reduce lifespan over time.

### Can I use any external SSD?

Yes, but Thunderbolt 4 SSDs provide the best performance. USB-C SSDs may also work but with lower speeds.

## MCP

### What is MCP?

MCP (Model Context Protocol) is a protocol for connecting AI assistants to external tools and data sources.

### Where is the MCP config stored?

Default path: `~/.config/mcp/servers.json`. You can change it with:

```bash
omni config set mcp_config_path /custom/path
```

## APIs

### Do I need API tokens?

Yes, for Hostinger, GitHub, and Unleash commands. Memory, MCP, and config commands work without tokens.

### Where do I get a Hostinger API token?

Log in to your Hostinger account and generate an API token in the developer/API section.

### Is my API token stored securely?

Tokens are stored in `~/.config/omni/config.toml` as plain text. Keep this file secure and do not commit it.

## Troubleshooting

### Where can I find help?

Check the [Troubleshooting Guide](TROUBLESHOOTING.md) or open an issue on GitHub.

## Contributing

### How can I contribute?

See the [Contributing Guide](CONTRIBUTING.md).
