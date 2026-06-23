# Omni CLI

**A CLI das CLIs** — Um hub unificado para orquestrar ferramentas de desenvolvimento.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/mateussiqueira/omni-cli/blob/main/LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-omni--cli-blue)](https://pypi.org/project/omni-cli/)
[![CI](https://github.com/mateussiqueira/omni-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/mateussiqueira/omni-cli/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://mateussiqueira.github.io/omni-cli/)

---

## O que é Omni CLI?

Omni CLI é uma **interface de linha de comando unificada** que conecta e orquestra múltiplas ferramentas de desenvolvimento em uma única interface consistente. Em vez de lembrar sintaxes diferentes para cada ferramenta, você usa uma CLI para governar todas.

```text
  ██████  ███    ███ ██ ███    ██
 ██    ██ ████  ████ ██ ████   ██
 ██    ██ ██ ████ ██ ██ ██ ██  ██
 ██    ██ ██  ██  ██ ██ ██  ██ ██
  ██████  ██      ██ ██ ██   ████
```

---

## Funcionalidades

### 🤖 IA e MCP
Gerencie servidores MCP (Model Context Protocol) para integração com ferramentas de IA — adicione, remova, teste e monitore sua infraestrutura de agentes de IA.

### 🧠 Otimização de Memória
Otimize a memória do macOS usando SSD Thunderbolt 4 como extensão de swap e cache. Monitore pressão de memória, mova caches de aplicativos e configure otimização automática.

### 🌐 Gerenciamento de Cloud
- **Hostinger** — Domínios, zonas DNS e gerenciamento de VPS
- **Cloudflare** — Registros DNS e purga de cache
- **AWS** — Operações S3, EC2 e Route53
- **Vercel** — Gerenciamento de projetos e deploys

### 🐙 GitHub
Gerenciamento de repositórios, trending e clonagem em lote — tudo da linha de comando.

### 🚦 Feature Flags
Gerencie feature flags do Unleash: alterne, crie, arquive e verifique o estado das flags entre ambientes.

### 🔌 Sistema de Plugins
Estenda o Omni CLI com plugins externos descobertos via entry points do Python. Instale, liste e remova plugins dinamicamente.

### 🎭 Perfis
Alterne entre configurações de desenvolvimento, homologação e produção com um único comando. Credenciais isoladas por perfil.

### ⚙️ Configuração Inteligente
Configuração centralizada via arquivos TOML e variáveis de ambiente. Fonte única de verdade para todas as ferramentas.

---

## Início Rápido

### Instalar

```bash
pip install omni-cli
```

Ou a partir do código fonte:

```bash
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli
pip install -e ".[dev]"
```

### Verificar

```bash
omni version
# Omni CLI version 0.1.0
```

### Explorar

```bash
omni status            # Status do sistema
omni --help            # Todos os comandos
omni memory status     # Status da memória
omni github trending   # Repos em alta no GitHub
```

---

## Grupos de Comandos

| Comando | Descrição |
|---------|-----------|
| `omni memory` | 🧠 Otimização de memória Mac |
| `omni mcp` | 🔌 Gerenciamento de servidores MCP |
| `omni hostinger` | 🌐 Gerenciamento Hostinger |
| `omni cloudflare` | ☁️ Gerenciamento Cloudflare |
| `omni aws` | 🌩️ Gerenciamento AWS |
| `omni vercel` | ▲ Gerenciamento Vercel |
| `omni github` | 🐙 Gerenciamento GitHub |
| `omni unleash` | 🚦 Feature flags Unleash |
| `omni plugins` | 🔌 Gerenciamento de plugins |
| `omni config` | ⚙️ Gerenciamento de configuração |
| `omni completion` | 🐚 Completamento de shell |
| `omni update` | 🚀 Auto-atualização |

---

## Documentação

- **[Primeiros Passos](GETTING_STARTED.pt.md)** — Primeiros passos com Omni CLI
- **[Instalação](INSTALLATION.pt.md)** — Guia de instalação detalhado
- **[Referência de Comandos](COMMANDS.pt.md)** — Referência completa de comandos
- **[Exemplos](EXAMPLES.pt.md)** — Exemplos práticos de uso
- **[Arquitetura](ARCHITECTURE.md)** — Arquitetura do projeto
- **[Casos de Uso](USE_CASES.pt.md)** — Cenários reais
- **[FAQ](FAQ.pt.md)** — Perguntas frequentes
- **[Solução de Problemas](TROUBLESHOOTING.pt.md)** — Problemas comuns

### Tópicos Avançados

- **[Mergulho na Memória](MEMORY_DEEP_DIVE.pt.md)** — Internals de memória macOS
- **[Integração MCP](MCP_INTEGRATION.pt.md)** — Integração com ferramentas de IA
- **[Desenvolvimento de Plugins](PLUGIN_DEVELOPMENT.pt.md)** — Crie plugins
- **[Configuração Empresarial](ENTERPRISE_SETUP.pt.md)** — Deploy em time/org
- **[Performance](PERFORMANCE.pt.md)** — Dicas de otimização
- **[Migração](MIGRATION.pt.md)** — Migrando de outras ferramentas

---

## Estrutura do Projeto

```text
omni-cli/
├── src/omni/
│   ├── cli.py              # Entrypoint principal
│   ├── commands/           # 12 módulos de comando
│   │   ├── memory.py       # Otimização de memória
│   │   ├── mcp.py          # Servidores MCP
│   │   ├── hostinger.py    # API Hostinger
│   │   ├── cloudflare.py   # API Cloudflare
│   │   ├── aws.py         # Operações AWS
│   │   ├── vercel.py       # Gerenciamento Vercel
│   │   ├── github.py       # API GitHub
│   │   ├── unleash.py      # Feature flags
│   │   ├── plugins.py      # Sistema de plugins
│   │   ├── config.py       # Configuração
│   │   ├── completion.py   # Completamento shell
│   │   └── update.py       # Auto-atualização
│   └── core/               # Framework core
│       ├── config.py       # Config Pydantic
│       ├── executor.py     # Executor shell
│       ├── logger.py       # Logging + audit
│       ├── plugins.py      # Descoberta de plugins
│       └── profiles.py     # Gerenciamento de perfis
├── tests/                  # Suite de testes
├── docs/                   # Documentação
├── assets/                 # Logos e imagens
└── pyproject.toml          # Config do projeto
```

---

## Licença

MIT &copy; [Mateus Siqueira](https://github.com/mateussiqueira)
