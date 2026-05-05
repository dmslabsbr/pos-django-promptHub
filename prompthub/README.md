# ⚡ PromptHub

Read in Portuguese: [README.pt-BR.md](README.pt-BR.md)

> A collaborative platform to create, share, and evaluate AI prompts.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?style=flat)
![Version](https://img.shields.io/badge/version-0.1.0-informational?style=flat)

---

## 📺 Showcase

Watch the usage example video: [https://youtu.be/jm3Hg_0tp84](https://youtu.be/jm3Hg_0tp84)

![PromptHub Dashboard](../img/PH1.png)
![PromptHub Detail](../img/PH2.png)

## 📦 Project Structure

```
prompthub/
├── config/              # Django settings, urls, wsgi
├── prompts/             # Main app: models, views, forms, urls, admin
├── accounts/            # Auth: register, login, logout
├── templates/           # HTML templates organized by app
├── .env.example         # Environment variables (template)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── gunicorn.conf.py     # Production server configuration
├── diagrama_er.md       # Mermaid ER Diagram
└── VERSION
```

---

## 🚀 Local Execution

### 1. Prerequisites
- Python 3.13+
- PostgreSQL 16+

### 2. Setup Environment

```bash
# Navigate to directory
cd prompthub

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database and Variables

```bash
# Create database and user in PostgreSQL
psql -U postgres -c "CREATE USER prompthub WITH PASSWORD 'prompthub1234';"
psql -U postgres -c "CREATE DATABASE prompthub OWNER prompthub;"

# Configure .env
cp .env.example .env
```

### 4. Migrations and Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start Server

```bash
python manage.py runserver
```

Access: **http://localhost:8000**

---

## 🐳 Running with Docker

```bash
# Start all services (App + DB)
docker compose up --build -d

# Create superuser
docker compose exec app python manage.py createsuperuser
```

Access: **https://app.prompthub.orb.local** (or your environment's local mapping).

---

## ✨ Features

- **Full CRUD:** Manage prompts with title, description, content, and category.
- **Rating System:** 1 to 5 star ratings with duplicate vote protection.
- **Authentication:** Secure registration and login system.
- **Filters & Sorting:** Browse by category and sort by relevance or date.
- **Premium UI:** Dark mode design with Glassmorphism, based on a modern Design System.
- **Prod-ready:** Configured with Gunicorn, Docker, and secure environment variables.

---

## 🎨 Design System

The project follows a strict style guide (see `UI guide.md` in the repository root) focused on:
- Colors: `Primary Cyan (#0ea5e9)`, `Surface Slate (#0f172a)`.
- Typography: `Inter`.
- Effects: `Backdrop blur` and `Soft shadows`.
