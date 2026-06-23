# Guia de Desenvolvimento de Plugins

Aprenda a estender o Omni CLI com comandos customizados.

## Índice

- [Arquitetura de Plugins](#arquitetura-de-plugins)
- [Criando um Plugin Simples](#criando-um-plugin-simples)
- [Registrando Plugins](#registrando-plugins)
- [Acessando Utilitários Core](#acessando-utilitarios-core)
- [Configuração de Plugins](#configuracao-de-plugins)
- [Distribuição](#distribuicao)

## Arquitetura de Plugins

O Omni CLI usa Typer para registro de comandos. Um plugin é simplesmente um módulo Python que expõe um app Typer.

```text
my_omni_plugin/
├── __init__.py
└── commands.py
```

## Criando um Plugin Simples

Crie `my_omni_plugin/commands.py`:

```python
import typer
from rich.console import Console

app = typer.Typer(help="Meu plugin customizado do Omni CLI")
console = Console()

@app.command("hello")
def hello(name: str = typer.Option("World", "--name", "-n")) -> None:
    """Diga olá do meu plugin."""
    console.print(f"[green]Olá, {name}![/green]")

@app.command("status")
def status() -> None:
    """Mostrar status do plugin."""
    console.print("[blue]Meu plugin está rodando[/blue]")
```

Crie `my_omni_plugin/__init__.py`:

```python
from my_omni_plugin.commands import app

__all__ = ["app"]
```

## Registrando Plugins

Plugins podem ser registrados via entry points no `pyproject.toml`:

```toml
[project.entry-points."omni.plugins"]
myplugin = "my_omni_plugin:app"
```

O Omni CLI descobrirá e registrará todos os plugins automaticamente.

### Registro manual (para desenvolvimento)

Edite `src/omni/cli.py`:

```python
from my_omni_plugin import app as my_plugin_app

app.add_typer(my_plugin_app, name="myplugin", help="Meu plugin customizado")
```

## Acessando Utilitários Core

Plugins podem reutilizar utilitários core do Omni CLI:

```python
from omni.core.config import config
from omni.core.executor import run_command

# Usar configuração
api_token = config.hostinger_api_token

# Rodar comandos shell
result = run_command(["git", "status"])
```

## Configuração de Plugins

Plugins podem definir suas próprias chaves de config:

```python
# Em my_omni_plugin/config_extension.py
from omni.core.config import config

# Acessar ou definir config customizada
my_setting = config.to_dict().get("myplugin_setting", "default")
```

Usuários definem valores via:

```bash
omni config set myplugin_setting value
```

## Distribuição

Publique seu plugin no PyPI:

```toml
[project]
name = "omni-cli-myplugin"
version = "0.1.0"
dependencies = ["omni-cli>=0.1.0"]

[project.entry-points."omni.plugins"]
myplugin = "my_omni_plugin:app"
```

Usuários instalam com:

```bash
pip install omni-cli-myplugin
```

## Boas Práticas

- Use Typer para estrutura de CLI
- Use Rich para output bonito
- Trate erros com elegância
- Adicione testes para seus comandos
- Documente os comandos do seu plugin
- Prefixe nomes de pacotes de plugin com `omni-cli-`
