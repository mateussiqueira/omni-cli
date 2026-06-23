# Performance e Benchmarks

Expectativas de performance e benchmarking para funcionalidades do Omni CLI.

## Índice

- [Performance do SSD Thunderbolt 4](#performance-do-ssd-thunderbolt-4)
- [SSD Interno vs Externo](#ssd-interno-vs-externo)
- [Fazendo Benchmark do Seu Setup](#fazendo-benchmark-do-seu-setup)
- [Impacto da Otimização de Memória](#impacto-da-otimizacao-de-memoria)
- [Melhorias Esperadas](#melhorias-esperadas)

## Performance do SSD Thunderbolt 4

O Thunderbolt 4 fornece até 40 Gbps de banda. A performance real do SSD depende da qualidade do drive.

### Velocidades típicas

| Tipo de SSD | Velocidade de Leitura | Velocidade de Escrita | Notas |
|-------------|----------------------|----------------------|-------|
| NVMe Thunderbolt 4 high-end | 2.800 MB/s | 2.300 MB/s | Melhor para swap/cache |
| NVMe Thunderbolt 3 mid-range | 2.000 MB/s | 1.800 MB/s | Muito bom |
| NVMe USB4 | 1.800 MB/s | 1.500 MB/s | Bom |
| NVMe USB 3.2 Gen 2 | 900 MB/s | 800 MB/s | Aceitável para uso leve |
| SATA SSD (USB) | 500 MB/s | 400 MB/s | Não recomendado para swap |

## SSD Interno vs Externo

Macs modernos usam SSDs internos muito rápidos. Um bom SSD Thunderbolt 4 externo pode chegar perto.

| Métrica | SSD Interno do Mac | SSD Thunderbolt 4 | Diferença |
|---------|-------------------|-------------------|-----------|
| Leitura | ~5.000 MB/s | ~2.800 MB/s | ~44% mais lento |
| Escrita | ~4.000 MB/s | ~2.300 MB/s | ~43% mais lento |
| Latência | Muito baixa | Baixa | Ligeiramente maior |
| Impacto de endurance no SSD interno | Alto | Reduzido | Benefício significativo |

## Fazendo Benchmark do Seu Setup

### Testar velocidade do disco

No macOS:

```bash
diskutil info /Volumes/ThunderboltSSD | grep "Protocol"

# Teste simples de escrita
time dd if=/dev/zero of=/Volumes/ThunderboltSSD/test-file bs=1m count=1024
rm /Volumes/ThunderboltSSD/test-file
```

### Testar impacto da pressão de memória

1. Execute uma workload pesada de memória
2. Monitore com o Omni CLI:

```bash
omni memory monitor
```

3. Compare performance com e sem cache externo

### Testar velocidade do swap

```bash
# Criar pressão de memória e medir uso de swap
stress-ng --vm 4 --vm-bytes 2G --timeout 60s
```

Monitore o uso de swap durante o teste.

## Impacto da Otimização de Memória

Mover caches de apps para SSD Thunderbolt pode liberar armazenamento interno significativo:

| Tipo de Cache | Tamanho Típico | SSD Interno Economizado |
|---------------|---------------|------------------------|
| Docker Desktop | 10-100 GB | Alto |
| Xcode DerivedData | 5-50 GB | Alto |
| Gradle | 1-10 GB | Médio |
| npm | 1-5 GB | Médio |
| Python pip | 0.5-2 GB | Baixo-Médio |

## Melhorias Esperadas

### Para desenvolvedores

- Mais espaço livre no SSD interno
- Menos desgaste do SSD interno
- Melhor performance sustentada sob pressão de memória
- Builds Docker mais rápidos quando cache está em SSD externo rápido

### Para criadores de conteúdo

- Mais espaço para arquivos de projeto no SSD interno
- Menor risco de ficar sem espaço em disco

### Ressalvas

- A migração inicial de caches leva tempo
- O SSD externo deve permanecer conectado durante o uso
- O primeiro acesso a caches movidos pode ser ligeiramente mais lento que o SSD interno
- Não substitui RAM insuficiente em todos os casos
