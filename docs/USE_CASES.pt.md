# Casos de Uso Reais

Cenários práticos onde o Omni CLI entrega valor.

## Índice

- [Desenvolvedor Solo](#desenvolvedor-solo)
- [Time de Desenvolvimento](#time-de-desenvolvimento)
- [Engenheiro DevOps](#engenheiro-devops)
- [Fundador de Startup](#fundador-de-startup)
- [Freelancer Gerenciando Vários Clientes](#freelancer-gerenciando-vários-clientes)
- [Engenheiro SRE / Plataforma](#engenheiro-sre--plataforma)

## Desenvolvedor Solo

**Perfil**: Um desenvolvedor trabalhando em múltiplos projetos em um MacBook.

**Desafios**:
- Rodar Docker, Xcode e Node.js simultaneamente
- SSD interno enchendo com caches
- Gerenciar VPS e domínios

**Solução Omni CLI**:

```bash
# Liberar espaço no SSD interno
omni memory setup --disk /Volumes/ThunderboltSSD
omni memory cache-move docker
omni memory cache-move npm
omni memory cache-move xcode

# Gerenciar infraestrutura
omni hostinger domains
omni hostinger vps
omni hostinger dns myproject.com

# Gerenciar código
omni github repos --user myuser
omni github clone myuser/myproject
```

**Benefícios**: Mais espaço livre, builds mais rápidos, ferramentas unificadas.

## Time de Desenvolvimento

**Perfil**: Um time compartilhando infraestrutura e workflows.

**Desafios**:
- Ferramentas consistentes entre membros
- Tokens e configurações compartilhadas
- Coordenação de feature flags

**Solução Omni CLI**:

```bash
# Config compartilhada do time
omni config set unleash_url https://unleash.empresa.com

# Workflow de feature flags
omni unleash create new-feature --project default
omni unleash toggle new-feature true --project dev
omni unleash flags --project production

# Descoberta de repositórios
omni github repos --user empresa-org
```

**Benefícios**: Comandos padronizados, onboarding mais fácil, releases coordenados.

## Engenheiro DevOps

**Perfil**: Engenheiro gerenciando infraestrutura cloud e deployments.

**Desafios**:
- Múltiplos domínios e registros DNS
- Gerenciamento de frota de VPS
- Operações de repositório

**Solução Omni CLI**:

```bash
# Verificação diária de infraestrutura
omni hostinger domains
omni hostinger vps
omni hostinger dns production.com

# Clonar repos de deployment
omni github clone org/infrastructure --dir ./infra
omni github clone org/deployment --dir ./deploy
```

**Benefícios**: Checagens rápidas no terminal, menos troca de contexto.

## Fundador de Startup

**Perfil**: Fundador gerenciando produto, infraestrutura e custos.

**Desafios**:
- Orçamento limitado para ferramentas caras
- Necessidade de velocidade
- Vários chapéis

**Solução Omni CLI**:

```bash
# Gerenciamento all-in-one
omni memory status
omni hostinger domains
omni github repos --user startup
omni unleash flags
```

**Benefícios**: Gratuito, open source, workflow unificado.

## Freelancer Gerenciando Vários Clientes

**Perfil**: Freelancer com projetos e contas de hospedagem separadas.

**Desafios**:
- Múltiplas contas Hostinger
- Diferentes organizações GitHub
- Troca de contexto

**Solução Omni CLI**:

```bash
# Cliente A
export OMNI_HOSTINGER_API_TOKEN=$CLIENT_A_TOKEN
omni hostinger domains

# Cliente B
export OMNI_HOSTINGER_API_TOKEN=$CLIENT_B_TOKEN
omni hostinger domains

# GitHub pessoal
omni github repos --user freelancer
```

**Benefícios**: Alterne contextos com variáveis de ambiente, sem GUI.

## Engenheiro SRE / Plataforma

**Perfil**: Engenheiro responsável por confiabilidade e monitoramento.

**Desafios**:
- Auditorias regulares de infraestrutura
- Pressão de memória em máquinas de monitoramento
- Resposta a incidentes

**Solução Omni CLI**:

```bash
# Script de verificação diária automatizado
#!/bin/bash
omni memory status >> /var/log/omni-daily.log
omni hostinger vps >> /var/log/omni-daily.log
omni unleash flags --project production >> /var/log/omni-daily.log
```

**Benefícios**: Checagens agendadas, logs consistentes, resposta rápida a incidentes.

## Padrões Comuns

### Verificação daily standup

```bash
omni github repos --user myuser
omni unleash flags --project default
omni memory status
```

### Verificação pré-deploy

```bash
omni hostinger dns production.com
omni unleash flags --project production
omni github trending --lang python
```

### Limpeza end-of-day

```bash
omni memory cache-move docker
omni memory status
```
