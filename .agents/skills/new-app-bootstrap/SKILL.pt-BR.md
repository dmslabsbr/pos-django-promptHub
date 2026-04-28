---
name: new-app-bootstrap
description: Cria a estrutura inicial de um novo aplicativo com README, VERSION, dependências, Docker, diagrama ER e testes. Use quando o usuário pedir criar um novo app, bootstrap, scaffold ou configurar estrutura inicial do projeto.
---

# Bootstrap de Novo App

Ao criar um novo aplicativo do zero, garantir que todos os itens abaixo existam. Não exibir código ao usuário a menos que solicitado; aplicar alterações via ferramentas.

## Checklist obrigatório

Copie e complete:

```
- [ ] README.md com instruções de instalação e execução
- [ ] Arquivo VERSION na raiz do projeto (semver, ex.: 0.1.0)
- [ ] requirements.txt ou package.json com dependências
- [ ] .env.example com todas as variáveis e explicações curtas
- [ ] docker-compose.yml (stack completa)
- [ ] docker-compose.app-only.yml (apenas app)
- [ ] Dockerfile para o app
- [ ] .dockerignore para o app/linguagem
- [ ] diagrama_er.md (diagrama ER Mermaid.js) na raiz do app
- [ ] funcoes.md na raiz do projeto (listar e explicar funções)
- [ ] tests/ com test_<modulo>.py (pytest)
```

## Propósito dos arquivos

| Arquivo / pasta | Propósito |
|-----------------|-----------|
| `README.md` | Instalação, execução e comandos de build |
| `VERSION` | Fonte única da versão; exibir na UI ou em `/version` |
| `requirements.txt` / `poetry.lock` | Dependências travadas |
| `.env.example` | Variáveis de ambiente necessárias; sem segredos |
| `docker-compose.yml` | Stack completa |
| `docker-compose.app-only.yml` | Apenas app (DB/serviços já existentes) |
| `Dockerfile` | Build da imagem do app |
| `diagrama_er.md` | Diagrama ER Mermaid; atualizar quando o schema mudar |
| `funcoes.md` | Lista e descrição breve de todas as funções |
| `tests/` | pytest; `test_<modulo>.py`; meta 80% de cobertura |

## Convenções

- **BD**: PK `id_nome_da_tabela`, FK `id_nome_da_tabela_key`. Usar transações em alterações em múltiplas tabelas.
- **Python**: 3.12+, venv/uv/poetry por projeto, type hints, docstrings estilo Google.
- **Código**: Escrever diretamente no arquivo alvo; adicionar docstrings e comentários objetivos.

## Opcional para trabalho técnico

- `analise.md`: Pontos críticos, decisões, Q&A (Markdown).
- `plano.md`: Tarefas pequenas e detalhadas; basear em analise.md e funcoes.md; atualizar conforme concluído.

Não inventar caminhos ou arquivos; confirmar com o usuário se a raiz do projeto ou o nome do app estiverem em dúvida.
