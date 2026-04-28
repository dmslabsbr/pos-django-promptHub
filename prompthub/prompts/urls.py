"""URLs do app prompts."""

from django.urls import path
from . import views

app_name = "prompts"

urlpatterns = [
    path("", views.PromptListView.as_view(), name="lista"),
    path("prompt/novo/", views.PromptCreateView.as_view(), name="criar"),
    path("prompt/<int:pk>/", views.PromptDetailView.as_view(), name="detalhe"),
    path("prompt/<int:pk>/editar/", views.PromptUpdateView.as_view(), name="editar"),
    path("prompt/<int:pk>/excluir/", views.PromptDeleteView.as_view(), name="excluir"),
    path("prompt/<int:pk>/avaliar/", views.avaliar_prompt, name="avaliar"),
]
