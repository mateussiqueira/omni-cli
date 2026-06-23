# Contribuindo com o Omni CLI

Obrigado pelo interesse em contribuir com o Omni CLI! Este documento fornece diretrizes para contribuição.

## Como Contribuir

### Reportando Bugs

Se encontrar um bug, por favor abra uma issue no GitHub com:

- Título e descrição claros
- Passos para reproduzir
- Comportamento esperado
- Comportamento atual
- Versão do Omni CLI (`omni --version`)
- Versão do Python e sistema operacional

### Sugerindo Funcionalidades

Sugestões de funcionalidades são bem-vindas! Abra uma issue descrevendo:

- O problema que você está tentando resolver
- Sua solução proposta
- Alternativas que você considerou

### Pull Requests

1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/funcionalidade-incriv`)
3. Faça suas alterações
4. Execute testes e linting:

```bash
make test
make lint
make type-check
```

5. Commit suas alterações com mensagens claras
6. Push para seu fork
7. Abra um Pull Request

## Setup de Desenvolvimento

```bash
git clone https://github.com/mateussiqueira/omni-cli.git
cd omni-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Estilo de Código

Usamos:
- **Black** para formatação de código
- **Ruff** para linting
- **MyPy** para type checking

Execute antes de commitar:

```bash
make format
make lint
make type-check
```

## Testes

Todas as novas funcionalidades devem incluir testes. Execute a suíte de testes com:

```bash
make test
```

## Documentação

Ao adicionar novos comandos ou funcionalidades, por favor atualize:

- O arquivo de comando relevante em `src/omni/commands/`
- `docs/COMMANDS.md` e `docs/COMMANDS.pt.md`
- `README.md` e `README.pt.md` se necessário
- Este guia se os processos de contribuição mudarem

## Mensagens de Commit

Use mensagens de commit claras e descritivas:

```text
Adiciona funcionalidade X ao comando Y

- Explicação detalhada
- Outro detalhe relevante
```

## Código de Conduta

Por favor, seja respeitoso e construtivo em todas as interações. Veja [CODE_OF_CONDUCT.md](https://github.com/mateussiqueira/omni-cli/blob/main/CODE_OF_CONDUCT.md).

## Dúvidas?

Sinta-se à vontade para abrir uma issue para discussão.
