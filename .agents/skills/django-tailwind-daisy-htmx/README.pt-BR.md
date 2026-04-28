# django-tailwind-daisy-htmx

![Cursor Skill](https://img.shields.io/badge/Cursor-Skill-00d4aa?style=flat) ![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django) ![Tailwind](https://img.shields.io/badge/Tailwind-38bdf8?style=flat&logo=tailwindcss) ![HTMX](https://img.shields.io/badge/HTMX-1d4ed8?style=flat)

Leia em inglês: [README.md](README.md)

Skill do Cursor que define **Django + Tailwind CDN + DaisyUI CDN + HTMX** para o projeto Nexus. Sem Node.js, npm, build ou SPA: apenas templates server-side e CSS/JS via CDN.

## Descrição

- **Django**: renderização server-side, views/templates, PostgreSQL existente (ex.: schema `projetos`).
- **TailwindCSS e DaisyUI**: somente via CDN (sem `package.json`, PostCSS ou Vite).
- **HTMX**: para atualizações parciais e interações assíncronas (`hx-get`, `hx-post`, `hx-target`, `hx-trigger`).

Use esta skill ao gerar UI, templates ou instruções de instalação do Nexus para que o agente não sugira Node, npm, React, shadcn/ui ou pipeline de build no front-end.

## Quando usar

- Gerar ou atualizar apps Django (ex.: “projetos”) com templates HTML.
- Adicionar UI com componentes Tailwind + DaisyUI.
- Adicionar interatividade (formulários, listas, modais) via HTMX.
- Escrever instruções de setup/execução (apenas Python/Django, sem Node).

## Regras (resumo)

1. **UI**: Tailwind + DaisyUI via CDN; sem frameworks CSS que exijam build.
2. **Templates**: includes do Django, partials, componentes DaisyUI.
3. **Interações**: HTMX para requisições e atualização do DOM.
4. **Proibido**: `node_modules`, `src/`, `dist/`, `package.json`, PostCSS, Vite, Webpack, React, Vue.

## Validação

Antes de sugerir qualquer alteração: *“Isso funciona sem Node.js, npm ou passo de build?”* Se não, não sugerir.

## Instruções completas

Ver [SKILL.md](SKILL.md) para o texto completo da regra e requisitos dos módulos Nexus.
