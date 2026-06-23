# Configuração para Empresas e Times

Guia para implantar e usar o Omni CLI em ambientes de times e empresas.

## Índice

- [Configuração Compartilhada](#configuração-compartilhada)
- [Perfis de Ambiente](#perfis-de-ambiente)
- [Gerenciamento de Segredos](#gerenciamento-de-segredos)
- [Integração com CI/CD](#integração-com-cicd)
- [Onboarding de Time](#onboarding-de-time)
- [Controle de Acesso](#controle-de-acesso)
- [Auditoria](#auditoria)

## Configuração Compartilhada

Times podem compartilhar uma configuração base do Omni CLI sem expor segredos.

### Criar uma config base do time

Crie `omni-team-config.toml`:

```toml
# Configurações compartilhadas
unleash_url = "https://unleash.empresa.com"
github_username = "company-bot"
mcp_config_path = "/opt/omni/mcp/servers.json"
thunderbolt_disk = "/Volumes/ThunderboltSSD"

# Segredos ficam vazios e são fornecidos via variáveis de ambiente
hostinger_api_token = ""
github_token = ""
unleash_api_token = ""
```

### Distribuir a config

Armazene a config compartilhada na documentação interna ou repositório de infraestrutura (sem segredos):

```bash
cp omni-team-config.toml /opt/omni/config.toml
chmod 640 /opt/omni/config.toml
```

### Segredos por usuário

Cada membro do time define seus próprios tokens:

```bash
export OMNI_HOSTINGER_API_TOKEN=""
export OMNI_GITHUB_TOKEN=""
export OMNI_UNLEASH_API_TOKEN=""
```

## Perfis de Ambiente

Use variáveis de ambiente para alternar entre ambientes:

```bash
# Perfil de produção
export OMNI_HOSTINGER_API_TOKEN=$PROD_HOSTINGER_TOKEN
export OMNI_UNLEASH_URL=https://unleash.prod.empresa.com

# Perfil de desenvolvimento
export OMNI_HOSTINGER_API_TOKEN=$DEV_HOSTINGER_TOKEN
export OMNI_UNLEASH_URL=https://unleash.dev.empresa.com
```

Você pode criar aliases no shell:

```bash
alias omni-prod='OMNI_HOSTINGER_API_TOKEN=$PROD_HOSTINGER_TOKEN OMNI_UNLEASH_URL=https://unleash.prod.empresa.com omni'
alias omni-dev='OMNI_HOSTINGER_API_TOKEN=$DEV_HOSTINGER_TOKEN OMNI_UNLEASH_URL=https://unleash.dev.empresa.com omni'
```

## Gerenciamento de Segredos

Para ambientes automatizados, use um gerenciador de segredos:

### Com 1Password

```bash
eval $(op signin)
export OMNI_HOSTINGER_API_TOKEN=$(op read "op://vault/hostinger-token/credential")
```

### Com HashiCorp Vault

```bash
export OMNI_HOSTINGER_API_TOKEN=$(vault kv get -field=token secret/omni/hostinger)
```

### Com AWS Secrets Manager

```bash
export OMNI_HOSTINGER_API_TOKEN=$(aws secretsmanager get-secret-value --secret-id omni/hostinger --query SecretString --output text)
```

## Integração com CI/CD

Use o Omni CLI em pipelines CI/CD para verificações de infraestrutura:

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

## Onboarding de Time

Novos membros do time devem:

1. Instalar o Omni CLI:

```bash
pipx install omni-cli
```

2. Copiar a config compartilhada ou executar:

```bash
omni config init
```

3. Definir segredos específicos do ambiente
4. Verificar acesso:

```bash
omni status
omni hostinger domains
```

## Controle de Acesso

### Permissões de token por função

| Função | Hostinger | GitHub | Unleash |
|--------|-----------|--------|---------|
| Developer | Read-only | Read-only | Read-only |
| DevOps | Read/Write | Read/Write | Toggle flags |
| Admin | Full access | Full access | Admin |

### Use contas separadas

Evite usar contas pessoais para operações do time. Crie service accounts ou bots:

- `company-bot` para GitHub
- Usuários de API Hostinger dedicados
- Service accounts do Unleash

## Auditoria

Rastreie o uso do Omni CLI em ambientes compartilhados:

```bash
# Habilitar audit logging
export OMNI_AUDIT_LOG=/var/log/omni/audit.log
mkdir -p /var/log/omni
```

Considere envolver comandos críticos:

```bash
#!/bin/bash
# omni-audit.sh
logger -t omni "User: $USER, Command: $*"
omni "$@"
```
