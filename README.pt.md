# 🌟 Omni CLI

![Omni CLI Banner](assets/banner.png)

> **A CLI das CLIs** — Hub unificado para orquestrar ferramentas de desenvolvimento.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-omni--cli-blue)](https://pypi.org/project/omni-cli/)
[![CI](https://github.com/mateussiqueira/omni-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/mateussiqueira/omni-cli/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-4%2F4%20passing-brightgreen)](tests)

```text
  ██████  ███    ███ ██ ███    ██
 ██    ██ ████  ████ ██ ████   ██
 ██    ██ ██ ████ ██ ██ ██ ██  ██
 ██    ██ ██  ██  ██ ██ ██  ██ ██
  ██████  ██      ██ ██ ██   ████
```

## 🚀 Visão Geral

O **Omni CLI** é um hub de linha de comando unificado que conecta e orquestra diversas ferramentas de desenvolvimento em uma única interface:

- 🧠 **Memory**: Otimização de memória do macOS com SSD Thunderbolt 4
- 🔌 **MCP**: Gerenciamento de servidores Model Context Protocol
- 🌐 **Hostinger**: Gestão de domínios, DNS e VPS
- 🐙 **GitHub**: Gerenciamento de repositórios, trending e clones
- 🚦 **Unleash**: Gerenciamento de feature flags
- ⚙️ **Config**: Configuração centralizada

## 📦 Instalação

### Via PyPI (recomendado)

```bash
pip install omni-cli
```

### Do source

```bash
# Clone o repositório
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli

# Crie o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instale em modo desenvolvimento
pip install -e ".[dev]"

# Ou instale diretamente
pip install .
```

## ⚡ Uso Rápido

```bash
# Ver status geral
omni status

# Ver versão
omni version

# Configuração inicial interativa
omni config init
```

## 🛠️ Desenvolvimento com Makefile

O Omni CLI inclui um `Makefile` com tarefas comuns de desenvolvimento:

```bash
make install-dev    # Instalar com dependências de desenvolvimento
make test           # Rodar testes
make lint           # Rodar linters
make format         # Formatar código
make type-check     # Rodar type checker
make build          # Build do pacote
make clean          # Remover artefatos de build
```

## 🐚 Shell Completion

Ative o tab completion para o Omni CLI:

```bash
# Bash
omni completion install bash
source ~/.bashrc

# Zsh
omni completion install zsh
source ~/.zshrc

# Ou veja instruções manuais
omni completion bash
omni completion zsh
```

## 📚 Documentação

- [Primeiros Passos](docs/GETTING_STARTED.pt.md)
- [Guia de Instalação](docs/INSTALLATION.pt.md)
- [Referência de Comandos](docs/COMMANDS.pt.md)
- [Arquitetura](docs/ARCHITECTURE.md) (EN)
- [Exemplos Avançados](docs/EXAMPLES.pt.md)
- [Omni Memory Deep Dive](docs/MEMORY_DEEP_DIVE.pt.md)
- [Guia de Integração MCP](docs/MCP_INTEGRATION.pt.md)
- [Configuração para Empresas e Times](docs/ENTERPRISE_SETUP.pt.md)
- [Performance e Benchmarks](docs/PERFORMANCE.pt.md)
- [Desenvolvimento de Plugins](docs/PLUGIN_DEVELOPMENT.pt.md)
- [Guia de Migração](docs/MIGRATION.pt.md)
- [Casos de Uso Reais](docs/USE_CASES.pt.md)
- [Guia de Segurança](docs/SECURITY.pt.md)
- [Troubleshooting](docs/TROUBLESHOOTING.pt.md)
- [Contribuição](docs/CONTRIBUTING.pt.md)
- [FAQ](docs/FAQ.pt.md)
- [Changelog](CHANGELOG.md) (EN)
- [English](README.md)

## 🧠 Comandos de Memória

Otimize o Mac usando SSD Thunderbolt 4 como extensão de memória:

```bash
# Ver status da memória
omni memory status

# Configurar SSD Thunderbolt
omni memory setup --disk /Volumes/ThunderboltSSD

# Iniciar monitoramento
omni memory monitor

# Mover cache de apps pesados
omni memory cache-move docker
```

## 🔌 Comandos MCP

Gerencie servidores MCP:

```bash
# Listar servidores
omni mcp list

# Adicionar servidor
omni mcp add meu-server npx -y @modelcontextprotocol/server-filesystem /caminho

# Remover servidor
omni mcp remove meu-server

# Testar servidor
omni mcp test meu-server
```

## 🌐 Comandos Hostinger

Gerencie sua infraestrutura Hostinger:

```bash
# Listar domínios
omni hostinger domains

# Listar VPS
omni hostinger vps

# Ver registros DNS
omni hostinger dns conecthu.com
```

Configure o token:

```bash
export OMNI_HOSTINGER_API_TOKEN=seu_token_aqui
```

## 🐙 Comandos GitHub

```bash
# Listar repositórios
omni github repos --user mateussiqueira

# Repositórios em trending
omni github trending --lang python

# Clonar repositório
omni github clone mateussiqueira/omni-cli
```

Configure:

```bash
export OMNI_GITHUB_TOKEN=seu_token_aqui
export OMNI_GITHUB_USERNAME=mateussiqueira
```

## 🚦 Comandos Unleash

```bash
# Listar feature flags
omni unleash flags --project default

# Criar feature flag
omni unleash create minha-flag --desc "Descrição da flag"

# Habilitar/desabilitar
omni unleash toggle minha-flag true
omni unleash toggle minha-flag false
```

Configure:

```bash
export OMNI_UNLEASH_URL=https://seu-unleash.com
export OMNI_UNLEASH_API_TOKEN=seu_token
```

## ⚙️ Configuração

O Omni CLI armazena configurações em `~/.config/omni/config.toml`.

```bash
# Configuração interativa
omni config init

# Ver configurações
omni config show

# Definir valor
omni config set thunderbolt_disk /Volumes/MeuSSD

# Ver variáveis de ambiente
omni config env
```

## 🧪 Testes

```bash
pytest
```

## 🏗️ Arquitetura

```text
omni-cli/
├── src/omni/
│   ├── cli.py              # Entrypoint principal
│   ├── commands/           # Comandos por domínio
│   │   ├── memory.py
│   │   ├── mcp.py
│   │   ├── hostinger.py
│   │   ├── github.py
│   │   ├── unleash.py
│   │   ├── config.py
│   │   └── completion.py
│   └── core/               # Core utilities
│       ├── config.py
│       └── executor.py
├── tests/                  # Testes
├── docs/                   # Documentação (EN & PT)
├── scripts/                # Scripts de shell completion
├── .github/workflows/      # Workflows de CI/CD
├── Makefile                # Tarefas de desenvolvimento
├── pyproject.toml          # Configuração do projeto
└── README.md               # Documentação principal
```

## 🌍 Países Líderes em Open Source

| Posição | País | Destaque |
|---------|------|----------|
| 1 | 🇺🇸 EUA | Maior quantidade de projetos e contribuidores |
| 2 | 🇨🇳 China | Grande base de desenvolvedores |
| 3 | 🇩🇪 Alemanha | Qualidade técnica, Linux, KDE |
| 4 | 🇬🇧 Reino Unido | Inovação em web e infraestrutura |
| 5 | 🇮🇳 Índia | Comunidade em rápido crescimento |
| 6 | 🇫🇷 França | Projetos europeus importantes |
| 7 | 🇨🇦 Canadá | Forte presença em IA e dados abertos |
| 8 | 🇧🇷 Brasil | Comunidade ativa, Python, PHP, JS |
| 9 | 🇯🇵 Japão | Ruby, infraestrutura |
| 10 | 🇷🇺 Rússia | Projetos de sistemas e segurança |

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Feito com 💙 por [Mateus Siqueira](https://github.com/mateussiqueira)
