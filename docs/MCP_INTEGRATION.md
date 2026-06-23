# MCP Integration Guide

Integrate Omni CLI managed MCP servers with AI assistants, editors, and IDEs.

## Table of Contents

- [What is MCP](#what-is-mcp)
- [Supported Clients](#supported-clients)
- [Adding Servers with Omni CLI](#adding-servers-with-omni-cli)
- [Claude Desktop](#claude-desktop)
- [Cursor](#cursor)
- [VS Code](#vs-code)
- [Windsurf](#windsurf)
- [Custom Clients](#custom-clients)
- [Troubleshooting MCP](#troubleshooting-mcp)

## What is MCP

Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs. Omni CLI helps you manage MCP server configurations centrally.

## Supported Clients

MCP servers configured through Omni CLI work with any client that supports the MCP standard, including:

- Claude Desktop
- Cursor
- VS Code with MCP extensions
- Windsurf
- Custom MCP clients

## Adding Servers with Omni CLI

```bash
# Filesystem access
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)

# SQLite database
omni mcp add sqlite npx -y @modelcontextprotocol/server-sqlite /path/to/db.sqlite

# GitHub
omni mcp add github npx -y @modelcontextprotocol/server-github

# Test the servers
omni mcp test filesystem
omni mcp test sqlite
omni mcp test github
```

## Claude Desktop

Claude Desktop reads MCP config from `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS.

### Share Omni CLI config with Claude

```bash
# Use the same config path
omni config set mcp_config_path ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Then add servers:

```bash
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)
```

Restart Claude Desktop after adding servers.

## Cursor

Cursor supports MCP through its settings.

1. Open Cursor Settings
2. Navigate to MCP/Extensions
3. Point to your Omni CLI managed config file
4. Add servers via Omni CLI:

```bash
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)/cursor-projects
```

## VS Code

Use the MCP extension for VS Code:

1. Install an MCP extension from the marketplace
2. Configure it to read from `~/.config/mcp/servers.json`
3. Manage servers with Omni CLI

```bash
omni config set mcp_config_path ~/.config/mcp/servers.json
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)/vscode-projects
```

## Windsurf

Windsurf reads MCP configuration from a JSON file.

1. Open Windsurf settings
2. Set MCP config path to your Omni CLI managed file
3. Add servers via Omni CLI

## Custom Clients

Any client reading the standard MCP servers JSON can use Omni CLI:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username"]
    }
  }
}
```

## Troubleshooting MCP

### Server not appearing in client

1. Verify the config path matches what the client expects
2. Restart the client completely
3. Test with `omni mcp test <name>`

### Permission errors

Ensure the paths you expose to MCP servers are accessible and that commands like `npx` are in your PATH.

### Multiple clients, one config

Use a shared config path and symlink individual client configs:

```bash
ln -s ~/.config/mcp/servers.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
