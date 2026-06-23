# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-22

### Added

- Initial release of Omni CLI
- Unified command-line hub for development tools
- Memory optimization commands for macOS with Thunderbolt 4 SSD support
- MCP (Model Context Protocol) server management
- Hostinger domain, DNS, and VPS management
- GitHub repository operations, trending, and cloning
- Unleash feature flag management
- Centralized configuration with `omni config`
- Interactive setup wizard
- Shell completion support for Bash and Zsh
- Makefile with common development tasks
- GitHub Actions CI/CD workflow
- PyPI release workflow
- Comprehensive documentation in English and Portuguese
- MIT License

### Infrastructure

- Project structure with `src/omni` layout
- pyproject.toml with build, lint, test, and format configuration
- pytest test suite with coverage reporting
- Black, Ruff, and MyPy configuration

## [Unreleased]

### Added

- Real plugin system with entry point discovery (`omni.plugins`)
- Plugin management commands: `omni plugins list/install/uninstall/create`
- Configuration profiles: `omni config profile create/use/list/delete/show`
- Self-update command: `omni update`
- Audit logging via `OMNI_AUDIT_LOG`
- Structured logging via `OMNI_LOG_LEVEL`
- Cloudflare integration: `omni cloudflare zones/dns/purge`
- AWS integration: `omni aws s3/ec2/route53/status`
- Vercel integration: `omni vercel projects/deployments/env`
- Extended test suite (19 tests)
- Logo, banner, favicon and social preview assets

### Changed

- READMEs updated with new commands and documentation links
- Architecture documentation updated

## [0.1.1] - 2026-06-22

### Planned

- Encrypted credential storage
- Web dashboard for monitoring
- More cloud provider integrations (DigitalOcean, Hetzner, Azure, GCP)
- Native installers (Homebrew, .deb, .rpm)
- Fish shell completion
