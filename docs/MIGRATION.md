# Migration Guide

Migrate from other tools to Omni CLI.

## Table of Contents

- [From Direct API Usage](#from-direct-api-usage)
- [From Multiple CLIs](#from-multiple-clis)
- [From Shell Scripts](#from-shell-scripts)
- [From Other Memory Tools](#from-other-memory-tools)
- [Migration Checklist](#migration-checklist)

## From Direct API Usage

If you currently use `curl` or custom scripts to call Hostinger, GitHub, or Unleash APIs:

### Before

```bash
curl -H "Authorization: Bearer $TOKEN" \
  https://developers.hostinger.com/api/domains/v1/domains
```

### After

```bash
omni hostinger domains
```

### Migration steps

1. Set your API tokens:

```bash
omni config set hostinger_api_token your_token
omni config set github_token your_token
omni config set unleash_api_token your_token
```

2. Replace curl calls with Omni CLI commands
3. Update documentation and runbooks
4. Test commands in a non-production environment first

## From Multiple CLIs

If your team uses separate tools for each service:

| Old Tool | Omni CLI Replacement |
|----------|---------------------|
| Custom Hostinger scripts | `omni hostinger` |
| `gh` CLI (basic operations) | `omni github` |
| Unleash dashboard (basic toggles) | `omni unleash` |
| Manual MCP config editing | `omni mcp` |
| Custom memory scripts | `omni memory` |

### Migration steps

1. Install Omni CLI alongside existing tools
2. Migrate one command group at a time
3. Create shell aliases during transition
4. Remove old tools after full migration

## From Shell Scripts

Convert shell scripts to Omni CLI commands:

### Before

```bash
#!/bin/bash
# check-memory.sh
vm_stat
sysctl vm.swapusage
df -h /
```

### After

```bash
#!/bin/bash
omni memory status
```

### Benefits

- Unified output format
- Built-in alerts
- Cross-platform compatibility
- Easier maintenance

## From Other Memory Tools

If you use tools like `memtest`, custom swap scripts, or manual cache relocation:

### Migrate to Omni CLI

```bash
# Replace manual Docker cache move
omni memory cache-move docker

# Replace manual swap monitoring
omni memory monitor

# Replace disk space checks
omni memory status
```

## Migration Checklist

- [ ] Install Omni CLI
- [ ] Configure API tokens
- [ ] Identify existing scripts and commands to replace
- [ ] Migrate one service at a time
- [ ] Update team documentation
- [ ] Train team members on new commands
- [ ] Archive old scripts
- [ ] Set up monitoring/auditing
- [ ] Verify everything works in production

## Rollback Plan

If you need to revert:

1. Keep old scripts in an archive directory
2. Document old command equivalents
3. Maintain API tokens for direct access
4. Test rollback procedures before they are needed
