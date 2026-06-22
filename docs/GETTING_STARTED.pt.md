# Primeiros Passos

Bem-vindo ao **Omni CLI** — a CLI das CLIs.

## Pré-requisitos

- Python 3.10 ou superior
- macOS, Linux ou Windows
- (Opcional) GitHub CLI (`gh`) para operações de repositório

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale o Omni CLI

```bash
pip install -e ".[dev]"
```

## Primeiros Passos

### 1. Verifique a instalação

```bash
omni version
```

Saída esperada:

```text
Omni CLI version 0.1.0
```

### 2. Execute o comando de status

```bash
omni status
```

### 3. Configure as credenciais

```bash
omni config init
```

Este comando interativo perguntará por:
- Token da API Hostinger
- Token e usuário do GitHub
- URL e token do Unleash
- Caminho do SSD Thunderbolt

Você também pode definir valores via variáveis de ambiente:

```bash
export OMNI_HOSTINGER_API_TOKEN=seu_token
export OMNI_GITHUB_TOKEN=seu_token
export OMNI_GITHUB_USERNAME=seu_usuario
export OMNI_UNLEASH_URL=https://seu-unleash.com
export OMNI_UNLEASH_API_TOKEN=seu_token
export OMNI_THUNDERBOLT_DISK=/Volumes/ThunderboltSSD
```

## Exemplos Rápidos

### Otimização de memória

```bash
omni memory status
omni memory setup --disk /Volumes/ThunderboltSSD
```

### Gerenciamento Hostinger

```bash
omni hostinger domains
omni hostinger vps
omni hostinger dns conecthu.com
```

### Operações GitHub

```bash
omni github repos --user mateussiqueira
omni github clone mateussiqueira/omni-cli
```

### Gerenciamento MCP

```bash
omni mcp list
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users
```

## Próximos Passos

- Leia a [Referência de Comandos](COMMANDS.pt.md)
- Conheça a [Arquitetura](ARCHITECTURE.md) (EN)
- Leia em [English](../README.md)
