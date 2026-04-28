# Diagrama ER — PromptHub

```mermaid
erDiagram
    auth_user {
        bigint id PK
        varchar username
        varchar email
        varchar password
    }

    prompts {
        bigint id PK
        varchar titulo
        text descricao
        text conteudo
        varchar categoria
        bigint id_autor FK
        timestamptz created_at
        timestamptz updated_at
    }

    avaliacoes {
        bigint id PK
        bigint id_prompt FK
        bigint id_usuario FK
        int nota
        timestamptz created_at
    }

    auth_user ||--o{ prompts : "cria"
    auth_user ||--o{ avaliacoes : "avalia"
    prompts ||--o{ avaliacoes : "recebe"
```

## Regras de negócio
- `avaliacoes(id_prompt, id_usuario)` é `UNIQUE` — um voto por usuário por prompt.
- O autor não pode avaliar seu próprio prompt (regra aplicada na view).
- `nota` aceita apenas valores entre 1 e 5 (validator no model + form).
