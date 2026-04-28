# django-tailwind-daisy-htmx

![Cursor Skill](https://img.shields.io/badge/Cursor-Skill-00d4aa?style=flat) ![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django) ![Tailwind](https://img.shields.io/badge/Tailwind-38bdf8?style=flat&logo=tailwindcss) ![HTMX](https://img.shields.io/badge/HTMX-1d4ed8?style=flat)

Read in Portuguese: [README.pt-BR.md](README.pt-BR.md)

Cursor skill that enforces **Django + Tailwind CDN + DaisyUI CDN + HTMX** for the Nexus project. No Node.js, npm, build step, or SPA: server-side templates only, with CDN-loaded CSS/JS.

## Description

- **Django**: server-side rendering, views/templates, existing PostgreSQL (e.g. schema `projetos`).
- **TailwindCSS & DaisyUI**: loaded via CDN only (no `package.json`, no PostCSS/Vite).
- **HTMX**: for partial updates and async interactions (`hx-get`, `hx-post`, `hx-target`, `hx-trigger`).

Use this skill when generating UI, templates, or install instructions for Nexus so the agent never suggests Node, npm, React, shadcn/ui, or any front-end build pipeline.

## When to use

- Generating or updating Django apps (e.g. “projetos”) with HTML templates.
- Adding UI with Tailwind + DaisyUI components.
- Adding interactive behavior (forms, lists, modals) via HTMX.
- Writing setup/run instructions (Python/Django only, no Node).

## Rules (summary)

1. **UI**: Tailwind + DaisyUI via CDN; no custom CSS frameworks that require build.
2. **Templates**: Django includes, partials, DaisyUI components.
3. **Interactions**: HTMX for requests and DOM updates.
4. **No**: `node_modules`, `src/`, `dist/`, `package.json`, PostCSS, Vite, Webpack, React, Vue.

## Validation

Before suggesting any change, ask: *“Does this work without Node.js, npm, or a build step?”* If not, do not suggest it.

## Full instructions

See [SKILL.md](SKILL.md) for the complete rule text and Nexus module requirements.
