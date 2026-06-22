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

## `omni status`

Mostrar status geral do Omni CLI.

## `omni version`

Mostrar versão do Omni CLI.
