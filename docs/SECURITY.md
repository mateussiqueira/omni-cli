# Security Guide

Security best practices for using Omni CLI safely.

## Table of Contents

- [Credential Storage](#credential-storage)
- [API Token Management](#api-token-management)
- [Least Privilege](#least-privilege)
- [Configuration File Security](#configuration-file-security)
- [Network Security](#network-security)
- [Audit and Monitoring](#audit-and-monitoring)
- [Reporting Security Issues](#reporting-security-issues)

## Credential Storage

Omni CLI stores configuration in `~/.config/omni/config.toml`. This file may contain sensitive API tokens.

### Protect your config file

```bash
# Set restrictive permissions (read/write only for owner)
chmod 600 ~/.config/omni/config.toml

# Never commit this file
# Ensure .gitignore excludes it
```

### Prefer environment variables for CI/CD

In automated environments, use environment variables instead of writing tokens to disk:

```bash
export OMNI_HOSTINGER_API_TOKEN="your-token"
export OMNI_GITHUB_TOKEN="your-token"
export OMNI_UNLEASH_API_TOKEN="your-token"
```

## API Token Management

### Hostinger

- Generate a dedicated API token with minimal permissions
- Use separate tokens for production and development
- Rotate tokens every 90 days
- Never share tokens in chat, email, or version control

### GitHub

- Create tokens at https://github.com/settings/tokens
- Use fine-grained personal access tokens when possible
- Required scopes:
  - `repo` — for private repository access
  - `read:user` — for user information
  - `read:org` — for organization repositories (if needed)

### Unleash

- Use environment-specific tokens (dev, staging, production)
- Restrict token permissions to read-only unless toggling flags
- Rotate admin tokens regularly

## Least Privilege

Apply the principle of least privilege:

- Use read-only tokens for monitoring commands
- Use write tokens only when modifying infrastructure
- Create separate Omni CLI profiles for different environments
- Avoid using admin/root tokens for daily operations

## Configuration File Security

Your `config.toml` should never be committed. Example safe setup:

```toml
hostinger_api_token = ""
github_token = ""
github_username = "mateussiqueira"
unleash_url = ""
unleash_api_token = ""
mcp_config_path = "~/.config/mcp/servers.json"
thunderbolt_disk = "/Volumes/ThunderboltSSD"
```

Set tokens via environment variables in production:

```bash
export OMNI_HOSTINGER_API_TOKEN=""
export OMNI_GITHUB_TOKEN=""
export OMNI_UNLEASH_API_TOKEN=""
```

## Network Security

- Only use trusted networks when transmitting API tokens
- Avoid using public Wi-Fi for infrastructure management
- Use a VPN when managing production resources remotely
- Ensure HTTPS is used for all API endpoints

## Audit and Monitoring

Monitor usage of Omni CLI in shared environments:

```bash
# Enable command logging
export OMNI_LOG_LEVEL=INFO

# Review logs regularly
ls ~/.config/omni/logs/
```

## Reporting Security Issues

If you discover a security vulnerability in Omni CLI, please:

1. Do not open a public issue
2. Email the maintainers directly
3. Provide a detailed description and reproduction steps
4. Allow reasonable time for disclosure

We take security seriously and will respond promptly.
