# Guia de Segurança

Melhores práticas de segurança para usar o Omni CLI com segurança.

## Índice

- [Armazenamento de Credenciais](#armazenamento-de-credenciais)
- [Gerenciamento de Tokens de API](#gerenciamento-de-tokens-de-api)
- [Privilégio Mínimo](#privilegio-minimo)
- [Segurança do Arquivo de Configuração](#seguranca-do-arquivo-de-configuracao)
- [Segurança de Rede](#seguranca-de-rede)
- [Auditoria e Monitoramento](#auditoria-e-monitoramento)
- [Reportando Problemas de Segurança](#reportando-problemas-de-seguranca)

## Armazenamento de Credenciais

O Omni CLI armazena configurações em `~/.config/omni/config.toml`. Este arquivo pode conter tokens de API sensíveis.

### Proteja seu arquivo de configuração

```bash
# Defina permissões restritivas (leitura/escrita apenas para o dono)
chmod 600 ~/.config/omni/config.toml

# Nunca commite este arquivo
# Certifique-se de que o .gitignore o exclui
```

### Prefira variáveis de ambiente para CI/CD

Em ambientes automatizados, use variáveis de ambiente em vez de escrever tokens em disco:

```bash
export OMNI_HOSTINGER_API_TOKEN="seu-token"
export OMNI_GITHUB_TOKEN="seu-token"
export OMNI_UNLEASH_API_TOKEN="seu-token"
```

## Gerenciamento de Tokens de API

### Hostinger

- Gere um token de API dedicado com permissões mínimas
- Use tokens separados para produção e desenvolvimento
- Rotacione tokens a cada 90 dias
- Nunca compartilhe tokens em chat, email ou version control

### GitHub

- Crie tokens em https://github.com/settings/tokens
- Use fine-grained personal access tokens quando possível
- Escopos necessários:
  - `repo` — para acesso a repositórios privados
  - `read:user` — para informações do usuário
  - `read:org` — para repositórios de organização (se necessário)

### Unleash

- Use tokens específicos por ambiente (dev, staging, production)
- Restrinja permissões de tokens para read-only a menos que esteja alternando flags
- Rotacione tokens admin regularmente

## Privilégio Mínimo

Aplique o princípio do privilégio mínimo:

- Use tokens read-only para comandos de monitoramento
- Use tokens de escrita apenas ao modificar infraestrutura
- Crie perfis separados do Omni CLI para diferentes ambientes
- Evite usar tokens admin/root para operações diárias

## Segurança do Arquivo de Configuração

Seu `config.toml` nunca deve ser commitado. Exemplo de configuração segura:

```toml
hostinger_api_token = ""
github_token = ""
github_username = "mateussiqueira"
unleash_url = ""
unleash_api_token = ""
mcp_config_path = "~/.config/mcp/servers.json"
thunderbolt_disk = "/Volumes/ThunderboltSSD"
```

Defina tokens via variáveis de ambiente em produção:

```bash
export OMNI_HOSTINGER_API_TOKEN=""
export OMNI_GITHUB_TOKEN=""
export OMNI_UNLEASH_API_TOKEN=""
```

## Segurança de Rede

- Use apenas redes confiáveis ao transmitir tokens de API
- Evite usar Wi-Fi público para gerenciamento de infraestrutura
- Use VPN ao gerenciar recursos de produção remotamente
- Certifique-se de que HTTPS seja usado para todos os endpoints de API

## Auditoria e Monitoramento

Monitore o uso do Omni CLI em ambientes compartilhados:

```bash
# Habilitar logging de comandos
export OMNI_LOG_LEVEL=INFO

# Revisar logs regularmente
ls ~/.config/omni/logs/
```

## Reportando Problemas de Segurança

Se descobrir uma vulnerabilidade de segurança no Omni CLI, por favor:

1. Não abra uma issue pública
2. Envie um email diretamente para os mantenedores
3. Forneça uma descrição detalhada e passos de reprodução
4. Permita um tempo razoável para divulgação

Levamos segurança a sério e responderemos prontamente.
