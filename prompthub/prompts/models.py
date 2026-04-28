"""Modelos do app prompts: Prompt e Avaliacao."""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Prompt(models.Model):
    """Prompt colaborativo criado por um usuário."""

    class Categoria(models.TextChoices):
        PROGRAMACAO = "programacao", "Programação"
        ESCRITA = "escrita", "Escrita"
        ANALISE = "analise", "Análise"
        EDUCACAO = "educacao", "Educação"
        MARKETING = "marketing", "Marketing"
        OUTROS = "outros", "Outros"

    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição", max_length=500)
    conteudo = models.TextField("Conteúdo do Prompt")
    categoria = models.CharField(
        "Categoria",
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.OUTROS,
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="prompts",
        verbose_name="Autor",
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        db_table = "prompts"
        ordering = ["-created_at"]
        verbose_name = "Prompt"
        verbose_name_plural = "Prompts"

    def __str__(self) -> str:
        return self.titulo

    def media_avaliacoes(self) -> float | None:
        """Retorna a média das avaliações ou None se não houver nenhuma."""
        resultado = self.avaliacoes.aggregate(media=Avg("nota"))
        return resultado["media"]

    def total_avaliacoes(self) -> int:
        """Retorna o total de avaliações do prompt."""
        return self.avaliacoes.count()


class Avaliacao(models.Model):
    """Avaliação de 1 a 5 estrelas de um prompt por um usuário."""

    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
        verbose_name="Prompt",
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
        verbose_name="Usuário",
    )
    nota = models.IntegerField(
        "Nota",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    created_at = models.DateTimeField("Avaliado em", auto_now_add=True)

    class Meta:
        db_table = "avaliacoes"
        # garante: um usuário → um voto por prompt
        unique_together = [("prompt", "usuario")]
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self) -> str:
        return f"{self.usuario.username} → {self.prompt.titulo} ({self.nota}★)"
