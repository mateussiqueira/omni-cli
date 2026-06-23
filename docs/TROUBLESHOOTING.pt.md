# Troubleshooting

Problemas comuns e soluções ao usar o Omni CLI.

## Índice

- [Problemas de Instalação](#problemas-de-instalacao)
- [Problemas de Permissão](#problemas-de-permissao)
- [Comandos de Memória](#comandos-de-memoria)
- [API Hostinger](#api-hostinger)
- [API GitHub](#api-github)
- [Servidores MCP](#servidores-mcp)
- [Shell Completion](#shell-completion)
- [Obter Ajuda](#obter-ajuda)

## Problemas de Instalação

### `pip install omni-cli` falha com "externally-managed-environment"

**Causa**: Distribuições modernas do Python impedem instalações system-wide.

**Soluções**:

```bash
# Opção 1: Use um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate
pip install omni-cli

# Opção 2: Use pipx
pip install pipx
pipx install omni-cli
```

### Comando não encontrado após instalação

**Causa**: O diretório de scripts do Python não está no PATH.

**Soluções**:

```bash
# macOS/Linux - adicione ao ~/.bashrc ou ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Ou com pipx
pipx ensurepath
```

Reinicie o terminal após fazer alterações.

## Problemas de Permissão

### `omni memory setup` requer sudo

**Causa**: Configurar swap e LaunchAgents system-wide requer privilégios de root.

**Solução**:

```bash
sudo omni memory setup --disk /Volumes/ThunderboltSSD
```

### Não consegue escrever no SSD Thunderbolt

**Causa**: O disco pode estar formatado como somente leitura ou pertencer a outro usuário.

**Solução**:

```bash
# Verificar permissões do disco
ls -ld /Volumes/ThunderboltSSD

# Corrigir permissões (se necessário)
sudo chown -R $(whoami) /Volumes/ThunderboltSSD
```

## Comandos de Memória

### `omni memory status` mostra "Thunderbolt SSD: Not connected"

**Causa**: O caminho do disco configurado não existe.

**Solução**:

```bash
# Verificar discos disponíveis
ls /Volumes/

# Atualizar o caminho
omni config set thunderbolt_disk /Volumes/NomeDoSeuDisco
```

### Criação do arquivo de swap falha

**Causa**: O macOS gerencia o swap automaticamente; arquivos de swap manuais são limitados.

**Solução**: Deixe o macOS gerenciar o swap automaticamente. Use o SSD Thunderbolt para caches de apps:

```bash
omni memory cache-move docker
omni memory cache-move gradle
```

## API Hostinger

### `omni hostinger domains` retorna erro de autenticação

**Causa**: O token da API Hostinger está ausente ou inválido.

**Solução**:

```bash
export OMNI_HOSTINGER_API_TOKEN=seu_token_aqui
# Ou
omni config set hostinger_api_token seu_token_aqui
```

### Rate limit da API excedido

**Causa**: Muitas requisições em pouco tempo.

**Solução**: Aguarde alguns minutos antes de tentar novamente. Evite rodar comandos em loops muito rápidos.

## API GitHub

### `omni github repos` mostra erro 401 ou 403

**Causa**: O token do GitHub está ausente, expirado ou sem permissões.

**Solução**:

1. Crie um token em https://github.com/settings/tokens
2. Configure:

```bash
export OMNI_GITHUB_TOKEN=seu_token_aqui
export OMNI_GITHUB_USERNAME=seu_usuario
```

### Repositórios privados não aparecem

**Causa**: O token não tem escopo `repo`.

**Solução**: Regenere seu token do GitHub com o escopo `repo` habilitado.

## Servidores MCP

### `omni mcp test` falha imediatamente

**Causa**: O comando do servidor MCP não está instalado ou não está no PATH.

**Solução**:

```bash
# Verifique se o comando existe
which npx
which docker

# Instale se necessário
npm install -g npx
```

### Arquivo de configuração MCP não encontrado

**Causa**: O caminho padrão não existe.

**Solução**:

```bash
# Defina um caminho customizado
omni config set mcp_config_path ~/.config/mcp/servers.json

# Ou crie o diretório padrão
mkdir -p ~/.config/mcp
```

## Shell Completion

### Completion não funciona após instalação

**Causa**: O arquivo de configuração do shell não foi recarregado.

**Solução**:

```bash
# Bash
source ~/.bashrc

# Zsh
source ~/.zshrc
```

### `omni completion install zsh` falha

**Causa**: O diretório site-functions do Zsh não existe ou requer sudo.

**Solução**:

```bash
# Crie o diretório
sudo mkdir -p /usr/local/share/zsh/site-functions

# Depois instale
omni completion install zsh
```

## Obter Ajuda

Se seu problema não estiver listado aqui:

1. Confira o [FAQ](FAQ.pt.md)
2. Leia a [Referência de Comandos](COMMANDS.pt.md)
3. Abra uma issue no GitHub: https://github.com/mateussiqueira/omni-cli/issues

Ao reportar problemas, inclua:
- Versão do Omni CLI (`omni --version`)
- Versão do Python (`python --version`)
- Sistema operacional
- Mensagem de erro completa
- Passos para reproduzir
