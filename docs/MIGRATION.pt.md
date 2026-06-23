# Guia de Migração

Migre de outras ferramentas para o Omni CLI.

## Índice

- [De Uso Direto de API](#de-uso-direto-de-api)
- [De Múltiplas CLIs](#de-múltiplas-clis)
- [De Shell Scripts](#de-shell-scripts)
- [De Outras Ferramentas de Memória](#de-outras-ferramentas-de-memória)
- [Checklist de Migração](#checklist-de-migração)

## De Uso Direto de API

Se você atualmente usa `curl` ou scripts customizados para chamar APIs Hostinger, GitHub ou Unleash:

### Antes

```bash
curl -H "Authorization: Bearer $TOKEN" \
  https://developers.hostinger.com/api/domains/v1/domains
```

### Depois

```bash
omni hostinger domains
```

### Passos de migração

1. Defina seus tokens de API:

```bash
omni config set hostinger_api_token seu_token
omni config set github_token seu_token
omni config set unleash_api_token seu_token
```

2. Substitua chamadas curl por comandos do Omni CLI
3. Atualize documentação e runbooks
4. Teste comandos em ambiente não-produção primeiro

## De Múltiplas CLIs

Se seu time usa ferramentas separadas para cada serviço:

| Ferramenta Antiga | Substituição Omni CLI |
|-------------------|----------------------|
| Scripts customizados Hostinger | `omni hostinger` |
| CLI `gh` (operações básicas) | `omni github` |
| Dashboard Unleash (toggles básicos) | `omni unleash` |
| Edição manual de config MCP | `omni mcp` |
| Scripts customizados de memória | `omni memory` |

### Passos de migração

1. Instale o Omni CLI junto com as ferramentas existentes
2. Migre um grupo de comandos por vez
3. Crie aliases no shell durante a transição
4. Remova ferramentas antigas após migração completa

## De Shell Scripts

Converta shell scripts para comandos do Omni CLI:

### Antes

```bash
#!/bin/bash
# check-memory.sh
vm_stat
sysctl vm.swapusage
df -h /
```

### Depois

```bash
#!/bin/bash
omni memory status
```

### Benefícios

- Formato de output unificado
- Alertas built-in
- Compatibilidade cross-platform
- Manutenção mais fácil

## De Outras Ferramentas de Memória

Se você usa ferramentas como `memtest`, scripts customizados de swap, ou realocação manual de cache:

### Migrar para Omni CLI

```bash
# Substituir movimentação manual de cache Docker
omni memory cache-move docker

# Substituir monitoramento manual de swap
omni memory monitor

# Substituir verificações de espaço em disco
omni memory status
```

## Checklist de Migração

- [ ] Instalar Omni CLI
- [ ] Configurar tokens de API
- [ ] Identificar scripts e comandos existentes para substituir
- [ ] Migrar um serviço por vez
- [ ] Atualizar documentação do time
- [ ] Treinar membros do time nos novos comandos
- [ ] Arquivar scripts antigos
- [ ] Configurar monitoramento/auditoria
- [ ] Verificar tudo em produção

## Plano de Rollback

Se precisar reverter:

1. Mantenha scripts antigos em um diretório de arquivo
2. Documente equivalentes dos comandos antigos
3. Mantenha tokens de API para acesso direto
4. Teste procedimentos de rollback antes que sejam necessários
