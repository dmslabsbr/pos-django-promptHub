"""Admin do app prompts."""

from django.contrib import admin
from .models import Prompt, Avaliacao


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "created_at")
    list_filter = ("categoria",)
    search_fields = ("titulo", "descricao", "autor__username")
    ordering = ("-created_at",)


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("prompt", "usuario", "nota", "created_at")
    list_filter = ("nota",)
    ordering = ("-created_at",)
