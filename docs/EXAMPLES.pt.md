# Exemplos Avançados

Exemplos práticos para casos de uso comuns do Omni CLI.

## Índice

- [Fluxo de Otimização de Memória](#fluxo-de-otimização-de-memória)
- [Gerenciamento de Servidores MCP](#gerenciamento-de-servidores-mcp)
- [Automação de Infraestrutura Hostinger](#automação-de-infraestrutura-hostinger)
- [Operações de Repositório GitHub](#operações-de-repositório-github)
- [Fluxo de Feature Flags Unleash](#fluxo-de-feature-flags-unleash)
- [Combinando Comandos](#combinando-comandos)

## Fluxo de Otimização de Memória

### Setup completo para um Mac de desenvolvimento

```bash
# 1. Verificar pressão de memória atual
omni memory status

# 2. Conectar e configurar SSD Thunderbolt 4
omni memory setup --disk /Volumes/ThunderboltSSD

# 3. Mover caches pesados de desenvolvimento
omni memory cache-move docker
omni memory cache-move gradle
omni memory cache-move npm

# 4. Iniciar monitoramento
omni memory monitor
```

### Automatizar realocação de cache no perfil do shell

Adicione ao `~/.zshrc` ou `~/.bashrc`:

```bash
# Omni CLI: caches no SSD Thunderbolt
export GRADLE_USER_HOME=/Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/gradle
export NPM_CONFIG_CACHE=/Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/npm-cache
```

## Gerenciamento de Servidores MCP

### Adicionar servidores MCP comuns

```bash
# Acesso ao sistema de arquivos
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)

# Banco de dados SQLite
omni mcp add sqlite npx -y @modelcontextprotocol/server-sqlite /caminho/para/database.db

# Servidor GitHub MCP
omni mcp add github npx -y @modelcontextprotocol/server-github

# Testar todos os servidores
omni mcp test filesystem
omni mcp test sqlite
omni mcp test github
```

### Backup da configuração MCP

```bash
cp ~/.config/mcp/servers.json ~/.config/mcp/servers.json.backup
```

## Automação de Infraestrutura Hostinger

### Setup completo de domínio + VPS

```bash
# Listar seus recursos
omni hostinger domains
omni hostinger vps

# Verificar registros DNS
omni hostinger dns conecthu.com

# (Use a API Hostinger ou dashboard para atualizar registros quando necessário)
```

### Encontrar IP da VPS para SSH

```bash
omni hostinger vps | grep "hostname-da-sua-vps"
```

## Operações de Repositório GitHub

### Fluxo diário

```bash
# Ver seus repositórios mais recentes
omni github repos --user mateussiqueira

# Encontrar projetos Python em trending
omni github trending --lang python

# Clonar um projeto útil
omni github clone owner/project-name --dir ./pasta-local
```

### Clonagem em lote a partir de uma lista

```bash
for repo in "mateussiqueira/omni-cli" "mateussiqueira/unleash" "mateussiqueira/easy-mcp-br"; do
    omni github clone "$repo" --dir "./$(basename $repo)"
done
```

## Fluxo de Feature Flags Unleash

### Processo de release com feature flags

```bash
# Criar feature flag para nova funcionalidade
omni unleash create new-checkout-flow --desc "Novo fluxo de checkout mobile"

# Habilitar no projeto de desenvolvimento
omni unleash toggle new-checkout-flow true --project dev

# Depois, habilitar em produção
omni unleash toggle new-checkout-flow true --project production

# Listar todas as flags
omni unleash flags --project production
```

### Desativar uma funcionalidade

```bash
# Desabilitar flag
omni unleash toggle legacy-auth false

# (Remova a flag do código e do dashboard Unleash quando seguro)
```

## Combinando Comandos

### Verificar tudo de uma vez

```bash
#!/bin/bash
# daily-check.sh

echo "=== Omni CLI Daily Check ==="
echo ""
echo "Memória:"
omni memory status

echo ""
echo "Servidores MCP:"
omni mcp list

echo ""
echo "Domínios Hostinger:"
omni hostinger domains

echo ""
echo "Repos GitHub:"
omni github repos
```

### Script de setup de ambiente

```bash
#!/bin/bash
# setup-dev-env.sh

# Configurar Omni CLI a partir de variáveis de ambiente
omni config set hostinger_api_token "$HOSTINGER_TOKEN"
omni config set github_token "$GITHUB_TOKEN"
omni config set github_username "$GITHUB_USER"
omni config set thunderbolt_disk "/Volumes/ThunderboltSSD"

echo "✅ Ambiente de desenvolvimento configurado"
```

## Dicas e Truques

### Alias para comandos comuns

Adicione ao seu perfil do shell:

```bash
alias omni-mem='omni memory status'
alias omni-repos='omni github repos --user mateussiqueira'
alias omni-flags='omni unleash flags --project default'
```

### Cron job para monitoramento de memória

```bash
# Verificar memória a cada hora e registrar
0 * * * * /usr/local/bin/omni memory status >> /var/log/omni-memory.log 2>&1
```

## Próximos Passos

- Leia o [Guia de Primeiros Passos](GETTING_STARTED.pt.md)
- Confira a [Referência de Comandos](COMMANDS.pt.md)
- Veja o [Troubleshooting](TROUBLESHOOTING.pt.md) se encontrar problemas
