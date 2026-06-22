# Guia de Instalação

Guia completo para instalar o Omni CLI em qualquer plataforma.

## Índice

- [Requisitos do Sistema](#requisitos-do-sistema)
- [Instalar via PyPI](#instalar-via-pypi)
- [Instalar do Source](#instalar-do-source)
- [Instalar com pipx](#instalar-com-pipx)
- [Instalar no macOS](#instalar-no-macos)
- [Instalar no Linux](#instalar-no-linux)
- [Instalar no Windows](#instalar-no-windows)
- [Verificar Instalação](#verificar-instalação)
- [Atualizar](#atualizar)
- [Desinstalar](#desinstalar)

## Requisitos do Sistema

- **Python**: 3.10 ou superior
- **Sistema Operacional**: macOS, Linux ou Windows
- **Espaço em Disco**: ~50 MB mínimo
- **RAM**: 512 MB mínimo (para operações da CLI)

## Instalar via PyPI

A forma mais fácil e recomendada de instalar o Omni CLI:

```bash
pip install omni-cli
```

Para instalar com dependências de desenvolvimento:

```bash
pip install "omni-cli[dev]"
```

### Usando pipx (Recomendado para CLIs)

O [pipx](https://pypa.github.io/pipx/) instala ferramentas CLI em ambientes isolados:

```bash
# Instale o pipx se não tiver
pip install pipx
pipx ensurepath

# Instale o Omni CLI
pipx install omni-cli
```

## Instalar do Source

Para desenvolvimento ou para obter funcionalidades ainda não lançadas:

```bash
# Clone o repositório
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli

# Crie um ambiente virtual
python3 -m venv .venv

# Ative o ambiente
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Instale em modo desenvolvimento
pip install -e ".[dev]"
```

## Instalar no macOS

### Usando Homebrew (quando disponível)

```bash
brew install omni-cli
```

### Usando pip

```bash
python3 -m pip install omni-cli
```

### Para Apple Silicon (M1/M2/M3)

O Omni CLI funciona nativamente no Apple Silicon. Se encontrar problemas de arquitetura, certifique-se de usar a versão arm64 do Python:

```bash
python3 -c "import platform; print(platform.machine())"
# Deve retornar: arm64
```

## Instalar no Linux

### Usando pip

```bash
python3 -m pip install omni-cli
```

### Usando o gerenciador de pacotes da distribuição (quando disponível)

```bash
# Ubuntu/Debian (quando .deb disponível)
sudo dpkg -i omni-cli_0.1.0_amd64.deb

# Fedora/RHEL (quando .rpm disponível)
sudo rpm -i omni-cli-0.1.0.x86_64.rpm
```

## Instalar no Windows

### Usando pip

```powershell
python -m pip install omni-cli
```

### Usando pipx

```powershell
pip install pipx
pipx ensurepath
pipx install omni-cli
```

Após a instalação, pode ser necessário reiniciar o terminal ou a sessão do PowerShell.

## Verificar Instalação

Execute os seguintes comandos para verificar a instalação:

```bash
# Verificar versão
omni --version

# Verificar status
omni status

# Mostrar ajuda
omni --help
```

Saída esperada para a versão:

```text
Omni CLI 0.1.0
```

## Atualizar

Para atualizar para a versão mais recente:

```bash
pip install --upgrade omni-cli
```

Ou com pipx:

```bash
pipx upgrade omni-cli
```

## Desinstalar

Para remover o Omni CLI:

```bash
pip uninstall omni-cli
```

Ou com pipx:

```bash
pipx uninstall omni-cli
```

## Pós-Instalação

Após instalar, execute a configuração interativa:

```bash
omni config init
```

Isso irá guiá-lo na configuração de:
- Token da API Hostinger
- Token e usuário do GitHub
- URL e token do Unleash
- Caminho do SSD Thunderbolt
- Caminho do config MCP

## Próximos Passos

- Leia o [Guia de Primeiros Passos](GETTING_STARTED.pt.md)
- Explore a [Referência de Comandos](COMMANDS.pt.md)
- Confira o [FAQ](FAQ.pt.md) para dúvidas comuns
