#!/usr/bin/env bash
# Executar na raiz do projeto: scripts/run0.sh [porta]

set -euo pipefail

PORT="${1:-8080}"

# Garante execução dentro do .venv do projeto
if [[ "${VIRTUAL_ENV:-}" == *"/.venv" ]]; then
  echo "✅ Ambiente virtual .venv já está ativo."
elif [[ -f ".venv/bin/activate" ]]; then
  echo "🔧 Ativando ambiente virtual .venv..."
  # shellcheck disable=SC1091
  source ".venv/bin/activate"
else
  echo "❌ Ambiente virtual não encontrado em .venv/bin/activate"
  echo "Crie/ative o .venv antes de executar este script."
  exit 1
fi

# Incrementa PATCH do arquivo VERSION (ex.: 0.7.1 -> 0.7.2)
if [[ -f "VERSION" ]]; then
  version_atual="$(tr -d '[:space:]' < VERSION | head -n 1)"
  IFS='.' read -r major minor patch <<< "${version_atual}"

  if [[ -n "${major:-}" && -n "${minor:-}" && -n "${patch:-}" && "${patch}" =~ ^[0-9]+$ ]]; then
    novo_patch="$((patch + 1))"
    nova_versao="${major}.${minor}.${novo_patch}"
    printf '%s\n' "${nova_versao}" > VERSION
    printf '📌 VERSION: %s -> %s\n' "${version_atual}" "${nova_versao}"
  fi
fi

echo "🧹 Apagando pastas __pycache__..."
find . -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true

echo "🗑️ Apagando arquivos .pyc..."
find . -type f -name "*.pyc" -delete 2>/dev/null || true

echo "🚀 Iniciando servidor Nexus na porta ${PORT}..."
python manage.py runserver_nexus "${PORT}"
