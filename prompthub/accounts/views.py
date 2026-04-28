"""Views de autenticação do app accounts."""

from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegistroForm


def registrar(request):
    """Cadastro de novo usuário."""
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"✅ Bem-vindo, {user.username}! Conta criada com sucesso.")
            return redirect("/")
    else:
        form = RegistroForm()

    return render(request, "accounts/registro.html", {"form": form})


def login_view(request):
    """Login de usuário existente."""
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"✅ Olá, {user.username}! Bem-vindo de volta.")
            next_url = request.GET.get("next", "/")
            return redirect(next_url)
        else:
            messages.error(request, "❌ Usuário ou senha incorretos.")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    """Logout com redirecionamento para página inicial."""
    auth.logout(request)
    messages.info(request, "👋 Você saiu com sucesso.")
    return redirect("/")
