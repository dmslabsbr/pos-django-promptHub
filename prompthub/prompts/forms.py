"""Formulários do app prompts."""

from django import forms
from .models import Prompt, Avaliacao


class PromptForm(forms.ModelForm):
    """Formulário para criar e editar prompts."""

    class Meta:
        model = Prompt
        fields = ["titulo", "descricao", "conteudo", "categoria"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título do prompt"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Breve descrição do que o prompt faz"}),
            "conteudo": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Cole aqui o conteúdo completo do prompt..."}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "titulo": "Título",
            "descricao": "Descrição",
            "conteudo": "Conteúdo",
            "categoria": "Categoria",
        }


class AvaliacaoForm(forms.ModelForm):
    """Formulário para avaliar um prompt (nota de 1 a 5)."""

    nota = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.HiddenInput(),
        label="Nota",
    )

    class Meta:
        model = Avaliacao
        fields = ["nota"]
