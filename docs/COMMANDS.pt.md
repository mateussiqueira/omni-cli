# Referência de Comandos

Referência completa dos comandos do Omni CLI.

## Opções Globais

```bash
omni --version     # Mostrar versão
omni --help        # Mostrar ajuda
```

## `omni memory`

Comandos de otimização de memória do macOS usando SSD Thunderbolt 4.

| Comando | Descrição |
|---------|-----------|
| `omni memory status` | Mostrar status atual da memória e swap |
| `omni memory setup` | Configurar SSD Thunderbolt como extensão de memória |
| `omni memory monitor` | Iniciar daemon de monitoramento de memória |
| `omni memory cache-move <app>` | Mover cache de app para SSD Thunderbolt |

### Exemplos

```bash
# Mostrar status da memória
omni memory status

# Configurar com disco customizado
omni memory setup --disk /Volumes/MeuSSD

# Mover cache do Docker
omni memory cache-move docker
```

## `omni mcp`

Gerenciamento de servidores Model Context Protocol.

| Comando | Descrição |
|---------|-----------|
| `omni mcp list` | Listar servidores MCP configurados |
| `omni mcp add <nome> <comando> [args...]` | Adicionar servidor MCP |
| `omni mcp remove <nome>` | Remover servidor MCP |
| `omni mcp test <nome>` | Testar servidor MCP |

### Exemplos

```bash
omni mcp list
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users
omni mcp test filesystem
omni mcp remove filesystem
```

## `omni hostinger`

Gerenciamento de infraestrutura Hostinger.

| Comando | Descrição |
|---------|-----------|
| `omni hostinger domains` | Listar domínios |
| `omni hostinger vps` | Listar instâncias VPS |
| `omni hostinger dns <dominio>` | Mostrar registros DNS |

### Ambiente

```bash
export OMNI_HOSTINGER_API_TOKEN=seu_token
```

## `omni github`

Operações do GitHub.

| Comando | Descrição |
|---------|-----------|
| `omni github repos [--user <usuario>]` | Listar repositórios |
| `omni github trending [--lang <lang>]` | Mostrar repositórios em trending |
| `omni github clone <repo> [--dir <dir>]` | Clonar um repositório |

### Ambiente

```bash
export OMNI_GITHUB_TOKEN=seu_token
export OMNI_GITHUB_USERNAME=seu_usuario
```

## `omni unleash`

Gerenciamento de feature flags do Unleash.

| Comando | Descrição |
|---------|-----------|
| `omni unleash flags [--project <id>]` | Listar feature flags |
| `omni unleash create <nome> [--desc <desc>]` | Criar feature flag |
| `omni unleash toggle <nome> <true|false>` | Alternar feature flag |

### Ambiente

```bash
export OMNI_UNLEASH_URL=https://seu-unleash.com
export OMNI_UNLEASH_API_TOKEN=seu_token
```

## `omni config`

Gerenciamento de configuração.

| Comando | Descrição |
|---------|-----------|
| `omni config show` | Mostrar configuração atual |
| `omni config set <key> <value>` | Definir valor de configuração |
| `omni config env` | Mostrar variáveis de ambiente |
| `omni config init` | Configuração inicial interativa |

### Exemplos

```bash
omni config init
omni config show
omni config set thunderbolt_disk /Volumes/ThunderboltSSD
```

## `omni cloudflare`

Gerenciamento de DNS e cache do Cloudflare.

| Comando | Descrição |
|---------|-----------|
| `omni cloudflare zones` | Listar zonas |
| `omni cloudflare dns <dominio>` | Listar registros DNS |
| `omni cloudflare purge <dominio>` | Limpar cache |

## `omni aws`

Gerenciamento de recursos AWS via AWS CLI.

| Comando | Descrição |
|---------|-----------|
| `omni aws status` | Verificar autenticação do AWS CLI |
| `omni aws s3` | Listar buckets S3 |
| `omni aws ec2 [--region <regiao>]` | Listar instâncias EC2 |
| `omni aws route53 [--zone <zone-id>]` | Listar zonas/records Route53 |

## `omni vercel`

Gerenciamento de projetos e deployments Vercel.

| Comando | Descrição |
|---------|-----------|
| `omni vercel projects` | Listar projetos |
| `omni vercel deployments [--project <nome>]` | Listar deployments |
| `omni vercel env <projeto>` | Listar variáveis de ambiente |

## `omni plugins`

Gerenciamento de plugins.

| Comando | Descrição |
|---------|-----------|
| `omni plugins list` | Listar plugins instalados |
| `omni plugins search <query>` | Buscar plugins |
| `omni plugins install <pacote>` | Instalar plugin |
| `omni plugins uninstall <pacote>` | Desinstalar plugin |
| `omni plugins create <nome>` | Criar template de plugin |

## `omni update`

Self-update do Omni CLI.

| Opção | Descrição |
|-------|-----------|
| `omni update --check` | Verificar atualizações |
| `omni update --force` | Forçar reinstalação |
| `omni update --dry-run` | Mostrar o que seria feito |

## `omni config profile`

Gerenciamento de perfis de configuração.

| Comando | Descrição |
|---------|-----------|
| `omni config profile list` | Listar perfis |
| `omni config profile create <nome> [--from <base>]` | Criar perfil |
| `omni config profile use <nome>` | Ativar perfil |
| `omni config profile delete <nome>` | Deletar perfil |
| `omni config profile show <nome>` | Mostrar config do perfil |

## `omni completion`

Configuração de shell completion.

| Comando | Descrição |
|---------|-----------|
| `omni completion bash` | Mostrar instruções do Bash completion |
| `omni completion zsh` | Mostrar instruções do Zsh completion |
| `omni completion install <bash\|zsh>` | Instalar completion automaticamente |

### Exemplos

```bash
omni completion install bash
omni completion install zsh
omni completion bash
```

## `omni status`

Mostrar status geral do Omni CLI.

## `omni version`

Mostrar versão do Omni CLI.
