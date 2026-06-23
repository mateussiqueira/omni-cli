# Omni Memory Deep Dive

Guia completo para entender e otimizar a memória do macOS com o Omni CLI e SSD Thunderbolt 4.

## Índice

- [Como o macOS Gerencia Memória](#como-o-macos-gerencia-memoria)
- [Por Que Usar um SSD Externo](#por-que-usar-um-ssd-externo)
- [Thunderbolt 4 vs Outras Interfaces](#thunderbolt-4-vs-outras-interfaces)
- [Estratégias de Configuração](#estrategias-de-configuracao)
- [Especificações Recomendadas de SSD](#especificacoes-recomendadas-de-ssd)
- [Monitorando a Pressão de Memória](#monitorando-a-pressao-de-memoria)
- [Movendo Caches de Apps](#movendo-caches-de-apps)
- [Configurações do macOS para Melhor Performance](#configuracoes-do-macos-para-melhor-performance)
- [Quando Não Usar Swap Externo](#quando-nao-usar-swap-externo)

## Como o macOS Gerencia Memória

O macOS usa várias técnicas de gerenciamento de memória:

- **Compressed Memory**: Comprime RAM inativa para liberar espaço
- **Swap**: Move dados inativos para o disco quando a RAM está cheia
- **Memory Pressure**: Indicador de quão duro o sistema está trabalhando para liberar RAM

Você pode verificar o status atual com:

```bash
omni memory status
memory_pressure
vm_stat
```

## Por Que Usar um SSD Externo

Quando a pressão de memória está alta, o macOS escreve swap no SSD interno. Isso pode:

- Deixar o sistema mais lento
- Desgastar o SSD interno mais rapidamente
- Reduzir o armazenamento interno disponível

Um SSD Thunderbolt 4 rápido externo pode:

- Descarregar swap e cache do armazenamento interno
- Fornecer velocidades próximas ao SSD interno
- Estender a vida útil do SSD interno
- Manter mais espaço livre no disco principal

## Thunderbolt 4 vs Outras Interfaces

| Interface | Velocidade Teórica | Velocidade Real | Bom para Swap? |
|-----------|-------------------|-----------------|----------------|
| Thunderbolt 4 | 40 Gbps | ~2.800 MB/s | ✅ Excelente |
| Thunderbolt 3 | 40 Gbps | ~2.500 MB/s | ✅ Excelente |
| USB4 | 40 Gbps | ~2.000 MB/s | ✅ Muito Bom |
| USB 3.2 Gen 2 | 10 Gbps | ~900 MB/s | ⚠️ Aceitável |
| USB 3.0 | 5 Gbps | ~400 MB/s | ❌ Muito lento |

## Estratégias de Configuração

### Estratégia 1: Caches de Apps no SSD Externo

Melhor para a maioria dos usuários. Mova caches pesados de apps sem modificar o swap do sistema:

```bash
omni memory cache-move docker
omni memory cache-move gradle
omni memory cache-move npm
omni memory cache-move xcode
```

### Estratégia 2: Extensão Completa de Memória

Para usuários avançados com pressão de memória sustentada:

```bash
omni memory setup --disk /Volumes/ThunderboltSSD
```

Isso configura monitoramento, logs e prepara o SSD para uso de swap/cache.

### Estratégia 3: Estação de Trabalho de Desenvolvedor

Combine ambas as estratégias para máximo benefício:

```bash
# Mover todos os caches de dev
omni memory cache-move docker
omni memory cache-move gradle
omni memory cache-move npm
omni memory cache-move xcode

# Configurar monitoramento
omni memory setup --disk /Volumes/ThunderboltSSD
omni memory monitor
```

## Especificações Recomendadas de SSD

Para resultados ideais, use um SSD com:

- **Interface**: Thunderbolt 4 ou Thunderbolt 3
- **Capacidade**: Pelo menos 1 TB (2 TB recomendado para workloads de dev)
- **Velocidade de Leitura/Escrita**: 2.000 MB/s+ sustentado
- **Cache DRAM**: Sim, para melhor performance sustentada
- **Endurance**: 600 TBW ou mais para modelos de 1 TB
- **Resfriamento**: Dissipador passivo ou ativo para cargas sustentadas

## Monitorando a Pressão de Memória

Use o Omni CLI para monitorar a memória continuamente:

```bash
omni memory monitor
```

O arquivo de log mostra:

```text
[2026-06-22 10:00:00] MEM: ... | SWAP: ... | PRESSURE: ... | DISK: ...
```

Interpretação dos níveis de pressão:

| RAM Livre | Status | Ação |
|-----------|--------|------|
| > 50% | 🟢 Baixa | Nenhuma necessária |
| 20-50% | 🟡 Média | Considere fechar apps |
| 10-20% | 🟠 Alta | Mova caches, reduza workload |
| < 10% | 🔴 Crítica | Ação imediata necessária |

## Movendo Caches de Apps

### Docker Desktop

```bash
# Nas configurações do Docker Desktop:
# Resources > Advanced > Disk image location
# Defina para: /Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/docker
```

### Xcode DerivedData

```bash
# No Xcode: Preferences > Locations > DerivedData
# Defina para: /Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/Xcode/DerivedData
```

### Gradle

```bash
export GRADLE_USER_HOME=/Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/gradle
```

### npm

```bash
npm config set cache /Volumes/ThunderboltSSD/.mac-memory-optimizer/apps/npm-cache
```

## Configurações do macOS para Melhor Performance

1. **Desativar "Colocar discos rígidos para dormir quando possível"**
   - Ajustes do Sistema > Economia de Energia
   - Isso mantém o SSD externo responsivo

2. **Habilitar Trim se suportado**
   - APFS moderno lida com isso automaticamente no Apple Silicon

3. **Manter 20% do SSD interno livre**
   - O macOS precisa de espaço livre para arquivos temporários e swap nativo

4. **Ejetar corretamente**
   - Sempre ejete o SSD Thunderbolt antes de desconectar para evitar perda de dados

## Quando Não Usar Swap Externo

Evite depender totalmente de SSD externo se:

- Seu SSD é USB 3.0 ou mais lento
- Você desconecta o SSD com frequência
- Seu SSD tem baixa endurance (TBW)
- Você trabalha com dados altamente sensíveis em drives portáteis

Nesses casos, foque em realocação de cache de apps e upgrade de RAM.
