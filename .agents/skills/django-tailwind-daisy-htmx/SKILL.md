---
name: django-tailwind-daisy-htmx
description: This is a new rule
---

<!--  Django + Tailwind CDN + DaisyUI CDN + HTMX. -->

# Overview

IMPORTANTE — LEIA COM ATENÇÃO ANTES DE GERAR QUALQUER CÓDIGO

Quero que você desenvolva os módulos do meu sistema Nexus, que é baseado em Django e usa renderização server-side com templates.

NÃO quero utilizar Node.js, npm, yarn, webpack, vite, postcss, build pipelines, React, Vue, shadcn/ui ou qualquer ambiente de front-end baseado em Node.

O AMBIENTE ATUAL É SIMPLES E DEVE PERMANECER ASSIM:

- Django + templates HTML
- TailwindCSS carregado via CDN (cdn.tailwindcss.com)
- DaisyUI carregado via CDN (sem instalação npm)
- HTMX carregado via CDN
- JavaScript mínimo, somente quando necessário
- NÃO instalar, configurar ou sugerir uso de Node.js
- NÃO gerar package.json, tailwind.config.js, postcss.config.js, vite.config.js ou qualquer arquivo de build
- NÃO criar estruturas SPA ou front-end separado
- O projeto deve funcionar totalmente sem build step.

OBJETIVO:

Crie o módulo “projetos” como um app Django, usando:

- Models mapeando tabelas JÁ EXISTENTES no PostgreSQL (schema projetos)
- Views Django ou Viewsets simples
- Templates HTML usando Tailwind + DaisyUI (via CDN) + HTMX para interações assíncronas
- URLs organizadas
- Partials para componentes de interface
- SEM introduzir dependências externas que exijam Node

COMPORTAMENTO ESPERADO DA IA:

1. Quando for gerar UI:
   - Usar Tailwind + DaisyUI diretamente via CDN.
   - NÃO gerar classes personalizadas extensas no CSS.
   - NÃO usar shadcn/ui, Material UI, React ou qualquer lib que exija build.

2. Quando for gerar templates:
   - Usar includes do Django, partials e componentes DaisyUI.

3. Quando for gerar interações:
   - Usar **HTMX** (hx-get, hx-post, hx-target, hx-trigger).

4. Quando for gerar assets:
   - NÃO criar pastas "src", "dist", "node_modules" ou similares.
   - NÃO gerar nada que dependa de npm ou Node.

5. Quando for gerar instruções de instalação:
   - Lembrar que o projeto utiliza apenas Python + Django, sem Node.
   - Tailwind, DaisyUI e HTMX serão sempre via CDN.

6. Garanta que todas as soluções funcionem usando:
   - Django renderizando páginas server-side
   - Tailwind CDN
   - DaisyUI CDN
   - HTMX

SEMPRE validar antes de sugerir qualquer coisa:
"Isso funciona sem Node.js? Sem npm? Sem build?"

Caso não funcione, NÃO sugerir.

Agora, com essas regras definidas, inicie o planejamento e implementação dos módulos do **Sistema Nexus** seguindo os arquivos de referência localizados na pasta referencia_ia/.
