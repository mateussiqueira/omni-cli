# Guia de Integração MCP

Integre servidores MCP gerenciados pelo Omni CLI com assistentes de IA, editores e IDEs.

## Índice

- [O Que é MCP](#o-que-é-mcp)
- [Clientes Suportados](#clientes-suportados)
- [Adicionando Servidores com Omni CLI](#adicionando-servidores-com-omni-cli)
- [Claude Desktop](#claude-desktop)
- [Cursor](#cursor)
- [VS Code](#vs-code)
- [Windsurf](#windsurf)
- [Clientes Customizados](#clientes-customizados)
- [Troubleshooting MCP](#troubleshooting-mcp)

## O Que é MCP

Model Context Protocol (MCP) é um protocolo aberto que padroniza como aplicações fornecem contexto para LLMs. O Omni CLI ajuda a gerenciar configurações de servidores MCP centralizadamente.

## Clientes Suportados

Servidores MCP configurados pelo Omni CLI funcionam com qualquer cliente que suporte o padrão MCP, incluindo:

- Claude Desktop
- Cursor
- VS Code com extensões MCP
- Windsurf
- Clientes MCP customizados

## Adicionando Servidores com Omni CLI

```bash
# Acesso ao sistema de arquivos
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)

# Banco de dados SQLite
omni mcp add sqlite npx -y @modelcontextprotocol/server-sqlite /caminho/para/db.sqlite

# GitHub
omni mcp add github npx -y @modelcontextprotocol/server-github

# Testar os servidores
omni mcp test filesystem
omni mcp test sqlite
omni mcp test github
```

## Claude Desktop

O Claude Desktop lê a configuração MCP de `~/Library/Application Support/Claude/claude_desktop_config.json` no macOS.

### Compartilhar config do Omni CLI com o Claude

```bash
# Use o mesmo caminho de config
omni config set mcp_config_path ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Depois adicione servidores:

```bash
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)
```

Reinicie o Claude Desktop após adicionar servidores.

## Cursor

O Cursor suporta MCP através de suas configurações.

1. Abra as Configurações do Cursor
2. Navegue até MCP/Extensions
3. Aponte para o arquivo de config gerenciado pelo Omni CLI
4. Adicione servidores via Omni CLI:

```bash
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)/cursor-projects
```

## VS Code

Use a extensão MCP para VS Code:

1. Instale uma extensão MCP do marketplace
2. Configure-a para ler de `~/.config/mcp/servers.json`
3. Gerencie servidores com o Omni CLI

```bash
omni config set mcp_config_path ~/.config/mcp/servers.json
omni mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/$(whoami)/vscode-projects
```

## Windsurf

O Windsurf lê a configuração MCP de um arquivo JSON.

1. Abra as configurações do Windsurf
2. Defina o caminho da config MCP para o arquivo gerenciado pelo Omni CLI
3. Adicione servidores via Omni CLI

## Clientes Customizados

Qualquer cliente que leia o JSON padrão de servidores MCP pode usar o Omni CLI:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username"]
    }
  }
}
```

## Troubleshooting MCP

### Servidor não aparece no cliente

1. Verifique se o caminho da config corresponde ao que o cliente espera
2. Reinicie o cliente completamente
3. Teste com `omni mcp test <nome>`

### Erros de permissão

Certifique-se de que os caminhos expostos aos servidores MCP sejam acessíveis e que comandos como `npx` estejam no PATH.

### Múltiplos clientes, uma config

Use um caminho de config compartilhado e crie symlinks para configs individuais de clientes:

```bash
ln -s ~/.config/mcp/servers.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
