"""Views do app prompts (class-based views + function views simples)."""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Count, QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Prompt, Avaliacao
from .forms import PromptForm, AvaliacaoForm


class PromptListView(ListView):
    """Página inicial: lista paginada de prompts com ordenação."""

    model = Prompt
    template_name = "prompts/lista.html"
    context_object_name = "prompts"
    paginate_by = 12

    def get_queryset(self) -> QuerySet:
        # Anota média e total de avaliações para exibição eficiente
        qs = Prompt.objects.select_related("autor").annotate(
            media=Avg("avaliacoes__nota"),
            total=Count("avaliacoes"),
        )

        # Filtro de categoria
        categoria = self.request.GET.get("categoria")
        if categoria:
            qs = qs.filter(categoria=categoria)

        # Ordenação
        ordem = self.request.GET.get("ordem", "recentes")
        if ordem == "avaliados":
            qs = qs.order_by("-media", "-created_at")
        else:
            qs = qs.order_by("-created_at")

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["ordem"] = self.request.GET.get("ordem", "recentes")
        ctx["categoria_selecionada"] = self.request.GET.get("categoria", "")
        ctx["categorias"] = Prompt.Categoria.choices
        return ctx


class PromptDetailView(DetailView):
    """Detalhe de um prompt com formulário de avaliação."""

    model = Prompt
    template_name = "prompts/detalhe.html"
    context_object_name = "prompt"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        prompt = self.object
        user = self.request.user

        # Dados de avaliação
        ctx["media"] = prompt.media_avaliacoes()
        ctx["total_avaliacoes"] = prompt.total_avaliacoes()
        ctx["form_avaliacao"] = AvaliacaoForm()

        # Verifica se o usuário logado já avaliou
        if user.is_authenticated:
            ctx["ja_avaliou"] = Avaliacao.objects.filter(prompt=prompt, usuario=user).exists()
            ctx["e_autor"] = prompt.autor == user
        else:
            ctx["ja_avaliou"] = False
            ctx["e_autor"] = False

        return ctx


class PromptCreateView(LoginRequiredMixin, CreateView):
    """Cria um novo prompt. Só para usuários autenticados."""

    model = Prompt
    form_class = PromptForm
    template_name = "prompts/form.html"
    success_url = reverse_lazy("prompts:lista")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "✅ Prompt criado com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["titulo_pagina"] = "Novo Prompt"
        ctx["btn_texto"] = "Publicar Prompt"
        return ctx


class PromptUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edita um prompt. Só o autor pode editar."""

    model = Prompt
    form_class = PromptForm
    template_name = "prompts/form.html"

    def test_func(self) -> bool:
        return self.get_object().autor == self.request.user

    def get_success_url(self):
        messages.success(self.request, "✅ Prompt atualizado com sucesso!")
        return reverse_lazy("prompts:detalhe", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["titulo_pagina"] = "Editar Prompt"
        ctx["btn_texto"] = "Salvar Alterações"
        return ctx


class PromptDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Exclui um prompt. Só o autor pode excluir."""

    model = Prompt
    template_name = "prompts/confirmar_exclusao.html"
    success_url = reverse_lazy("prompts:lista")
    context_object_name = "prompt"

    def test_func(self) -> bool:
        return self.get_object().autor == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "🗑️ Prompt excluído com sucesso!")
        return super().form_valid(form)


@login_required
def avaliar_prompt(request, pk: int):
    """Registra ou atualiza a avaliação de um prompt."""
    prompt = get_object_or_404(Prompt, pk=pk)

    # Autor não pode avaliar seu próprio prompt
    if prompt.autor == request.user:
        messages.error(request, "❌ Você não pode avaliar seu próprio prompt.")
        return redirect("prompts:detalhe", pk=pk)

    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            nota = form.cleaned_data["nota"]
            _, created = Avaliacao.objects.update_or_create(
                prompt=prompt,
                usuario=request.user,
                defaults={"nota": nota},
            )
            if created:
                messages.success(request, f"⭐ Avaliação registrada: {nota} estrela(s)!")
            else:
                messages.info(request, f"⭐ Avaliação atualizada para {nota} estrela(s).")
        else:
            messages.error(request, "❌ Nota inválida. Escolha entre 1 e 5.")

    return redirect("prompts:detalhe", pk=pk)
