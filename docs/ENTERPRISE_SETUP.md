# Enterprise and Team Setup

Guide for deploying and using Omni CLI in team and enterprise environments.

## Table of Contents

- [Shared Configuration](#shared-configuration)
- [Environment Profiles](#environment-profiles)
- [Secret Management](#secret-management)
- [CI/CD Integration](#cicd-integration)
- [Team Onboarding](#team-onboarding)
- [Access Control](#access-control)
- [Audit Logging](#audit-logging)

## Shared Configuration

Teams can share a base Omni CLI configuration without exposing secrets.

### Create a team base config

Create `omni-team-config.toml`:

```toml
# Shared settings
unleash_url = "https://unleash.company.com"
github_username = "company-bot"
mcp_config_path = "/opt/omni/mcp/servers.json"
thunderbolt_disk = "/Volumes/ThunderboltSSD"

# Secrets are left empty and provided via environment variables
hostinger_api_token = ""
github_token = ""
unleash_api_token = ""
```

### Distribute the config

Store the shared config in your team's internal documentation or infrastructure repository (without secrets):

```bash
cp omni-team-config.toml /opt/omni/config.toml
chmod 640 /opt/omni/config.toml
```

### Per-user secrets

Each team member sets their own tokens:

```bash
export OMNI_HOSTINGER_API_TOKEN=""
export OMNI_GITHUB_TOKEN=""
export OMNI_UNLEASH_API_TOKEN=""
```

## Environment Profiles

Use environment variables to switch between environments:

```bash
# Production profile
export OMNI_HOSTINGER_API_TOKEN=$PROD_HOSTINGER_TOKEN
export OMNI_UNLEASH_URL=https://unleash.prod.company.com

# Development profile
export OMNI_HOSTINGER_API_TOKEN=$DEV_HOSTINGER_TOKEN
export OMNI_UNLEASH_URL=https://unleash.dev.company.com
```

You can create shell aliases:

```bash
alias omni-prod='OMNI_HOSTINGER_API_TOKEN=$PROD_HOSTINGER_TOKEN OMNI_UNLEASH_URL=https://unleash.prod.company.com omni'
alias omni-dev='OMNI_HOSTINGER_API_TOKEN=$DEV_HOSTINGER_TOKEN OMNI_UNLEASH_URL=https://unleash.dev.company.com omni'
```

## Secret Management

For automated environments, use a secret manager:

### With 1Password

```bash
eval $(op signin)
export OMNI_HOSTINGER_API_TOKEN=$(op read "op://vault/hostinger-token/credential")
```

### With HashiCorp Vault

```bash
export OMNI_HOSTINGER_API_TOKEN=$(vault kv get -field=token secret/omni/hostinger)
```

### With AWS Secrets Manager

```bash
export OMNI_HOSTINGER_API_TOKEN=$(aws secretsmanager get-secret-value --secret-id omni/hostinger --query SecretString --output text)
```

## CI/CD Integration

Use Omni CLI in CI/CD pipelines for infrastructure checks:

```yaml
# .github/workflows/infra-check.yml
name: Infrastructure Check
on:
  schedule:
    - cron: '0 9 * * *'

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install omni-cli
      - run: |
          omni hostinger domains
          omni hostinger vps
        env:
          OMNI_HOSTINGER_API_TOKEN: ${{ secrets.HOSTINGER_TOKEN }}
```

## Team Onboarding

New team members should:

1. Install Omni CLI:

```bash
pipx install omni-cli
```

2. Copy the shared config or run:

```bash
omni config init
```

3. Set environment-specific secrets
4. Verify access:

```bash
omni status
omni hostinger domains
```

## Access Control

### Token permissions by role

| Role | Hostinger | GitHub | Unleash |
|------|-----------|--------|---------|
| Developer | Read-only | Read-only | Read-only |
| DevOps | Read/Write | Read/Write | Toggle flags |
| Admin | Full access | Full access | Admin |

### Use separate accounts

Avoid using personal accounts for team operations. Create service accounts or bots:

- `company-bot` for GitHub
- Dedicated Hostinger API users
- Unleash service accounts

## Configuration Profiles

Use profiles to switch between environments:

```bash
# Create production profile
omni config profile create production
omni config set hostinger_api_token $PROD_HOSTINGER_TOKEN
omni config set unleash_url https://unleash.prod.company.com

# Create development profile
omni config profile create development
omni config set hostinger_api_token $DEV_HOSTINGER_TOKEN
omni config set unleash_url https://unleash.dev.company.com

# Switch profiles
omni config profile use production
omni config profile use development
```

## Audit Logging

Omni CLI supports audit logging via the `OMNI_AUDIT_LOG` environment variable:

```bash
# Enable audit logging
export OMNI_AUDIT_LOG=/var/log/omni/audit.log
mkdir -p /var/log/omni

# All commands are now logged
omni hostinger domains
omni unleash flags
```

Example audit log entry:

```text
2026-06-22T20:00:00+00:00 - user=john command=omni hostinger domains
```

Consider wrapping critical commands for additional syslog integration:

```bash
#!/bin/bash
# omni-audit.sh
logger -t omni "User: $USER, Command: $*"
omni "$@"
```

## Logging Levels

Control Omni CLI internal logging:

```bash
export OMNI_LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
omni status
```

Logs are written to `~/.config/omni/logs/omni.log` when writable.
