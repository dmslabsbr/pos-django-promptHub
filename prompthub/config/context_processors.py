"""
Context processors globais do PromptHub.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def app_version(request):
    """Injeta a versão do app (arquivo VERSION) em todos os templates."""
    try:
        version = (BASE_DIR / "VERSION").read_text().strip()
    except FileNotFoundError:
        version = "?"
    return {"APP_VERSION": version}
