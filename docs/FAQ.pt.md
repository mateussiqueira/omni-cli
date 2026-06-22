# Perguntas Frequentes (FAQ)

## Geral

### O que é o Omni CLI?

O Omni CLI é um hub de linha de comando unificado que conecta múltiplas ferramentas de desenvolvimento (otimização de memória, MCP, Hostinger, GitHub, Unleash) em uma única interface.

### O Omni CLI é gratuito?

Sim, o Omni CLI é open source e gratuito sob a licença MIT.

### Quais plataformas são suportadas?

macOS, Linux e Windows com Python 3.10 ou superior.

## Instalação

### Posso instalar o Omni CLI sem sudo?

Sim, usar um ambiente virtual ou pipx é recomendado e não requer sudo.

```bash
pipx install omni-cli
```

### Posso instalar várias versões?

O ideal é usar ambientes virtuais para diferentes versões.

## Memória

### O Omni CLI aumenta minha RAM física?

Não. O Omni CLI ajuda a otimizar o uso de memória movendo caches pesados para um SSD Thunderbolt 4 externo e monitorando a pressão de memória.

### Usar um SSD externo como swap vai danificá-lo?

SSDs têm resistência finita a escrita. Um SSD Thunderbolt 4 de alta qualidade com cache DRAM e boa classificação de endurance pode lidar bem com operações de swap, mas swapping intensivo pode reduzir a vida útil ao longo do tempo.

### Posso usar qualquer SSD externo?

Sim, mas SSDs Thunderbolt 4 oferecem o melhor desempenho. SSDs USB-C também funcionam, mas com velocidades menores.

## MCP

### O que é MCP?

MCP (Model Context Protocol) é um protocolo para conectar assistentes de IA a ferramentas e fontes de dados externas.

### Onde a configuração MCP é armazenada?

Caminho padrão: `~/.config/mcp/servers.json`. Você pode alterar com:

```bash
omni config set mcp_config_path /caminho/customizado
```

## APIs

### Preciso de tokens de API?

Sim, para comandos Hostinger, GitHub e Unleash. Comandos de memória, MCP e config funcionam sem tokens.

### Onde consigo um token da API Hostinger?

Faça login na sua conta Hostinger e gere um token de API na seção de desenvolvedor/API.

### Meu token de API está armazenado de forma segura?

Os tokens são armazenados em `~/.config/omni/config.toml` como texto simples. Mantenha este arquivo seguro e não o commite.

## Troubleshooting

### Onde posso encontrar ajuda?

Confira o [Guia de Troubleshooting](TROUBLESHOOTING.pt.md) ou abra uma issue no GitHub.

## Contribuição

### Como posso contribuir?

Veja o [Guia de Contribuição](CONTRIBUTING.pt.md).
