# Real-World Use Cases

Practical scenarios where Omni CLI delivers value.

## Table of Contents

- [Solo Developer](#solo-developer)
- [Development Team](#development-team)
- [DevOps Engineer](#devops-engineer)
- [Startup Founder](#startup-founder)
- [Freelancer Managing Multiple Clients](#freelancer-managing-multiple-clients)
- [SRE / Platform Engineer](#sre-platform-engineer)

## Solo Developer

**Profile**: One developer working on multiple projects on a MacBook.

**Challenges**:
- Running Docker, Xcode, and Node.js simultaneously
- Internal SSD filling up with caches
- Managing VPS and domains

**Omni CLI solution**:

```bash
# Free up internal SSD
omni memory setup --disk /Volumes/ThunderboltSSD
omni memory cache-move docker
omni memory cache-move npm
omni memory cache-move xcode

# Manage infrastructure
omni hostinger domains
omni hostinger vps
omni hostinger dns myproject.com

# Manage code
omni github repos --user myuser
omni github clone myuser/myproject
```

**Benefits**: More free space, faster builds, unified tooling.

## Development Team

**Profile**: A team sharing infrastructure and workflows.

**Challenges**:
- Consistent tooling across members
- Shared API tokens and configurations
- Feature flag coordination

**Omni CLI solution**:

```bash
# Shared team config
omni config set unleash_url https://unleash.company.com

# Feature flag workflow
omni unleash create new-feature --project default
omni unleash toggle new-feature true --project dev
omni unleash flags --project production

# Repository discovery
omni github repos --user company-org
```

**Benefits**: Standardized commands, easier onboarding, coordinated releases.

## DevOps Engineer

**Profile**: Engineer managing cloud infrastructure and deployments.

**Challenges**:
- Multiple domains and DNS records
- VPS fleet management
- Repository operations

**Omni CLI solution**:

```bash
# Daily infrastructure check
omni hostinger domains
omni hostinger vps
omni hostinger dns production.com

# Clone deployment repos
omni github clone org/infrastructure --dir ./infra
omni github clone org/deployment --dir ./deploy
```

**Benefits**: Quick checks from terminal, less context switching.

## Startup Founder

**Profile**: Founder managing product, infrastructure, and costs.

**Challenges**:
- Limited budget for expensive tools
- Need to move fast
- Multiple hats

**Omni CLI solution**:

```bash
# All-in-one management
omni memory status
omni hostinger domains
omni github repos --user startup
omni unleash flags
```

**Benefits**: Free, open-source, unified workflow.

## Freelancer Managing Multiple Clients

**Profile**: Freelancer with separate projects and hosting accounts.

**Challenges**:
- Multiple Hostinger accounts
- Different GitHub organizations
- Context switching

**Omni CLI solution**:

```bash
# Client A
export OMNI_HOSTINGER_API_TOKEN=$CLIENT_A_TOKEN
omni hostinger domains

# Client B
export OMNI_HOSTINGER_API_TOKEN=$CLIENT_B_TOKEN
omni hostinger domains

# Personal GitHub
omni github repos --user freelancer
```

**Benefits**: Switch contexts with environment variables, no GUI needed.

## SRE / Platform Engineer

**Profile**: Engineer responsible for reliability and monitoring.

**Challenges**:
- Regular infrastructure audits
- Memory pressure on monitoring machines
- Incident response

**Omni CLI solution**:

```bash
# Automated daily check script
#!/bin/bash
omni memory status >> /var/log/omni-daily.log
omni hostinger vps >> /var/log/omni-daily.log
omni unleash flags --project production >> /var/log/omni-daily.log
```

**Benefits**: Scheduled checks, consistent logs, fast incident response.

## Common Patterns

### Daily standup check

```bash
omni github repos --user myuser
omni unleash flags --project default
omni memory status
```

### Pre-deploy verification

```bash
omni hostinger dns production.com
omni unleash flags --project production
omni github trending --lang python
```

### End-of-day cleanup

```bash
omni memory cache-move docker
omni memory status
```
