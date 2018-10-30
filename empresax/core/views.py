from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        if request.POST.get('nome') and request.POST.get('senha'):
            user = Usuario()
            user.nome = request.POST['nome']
            user.senha = request.POST['senha']
            user.save()
            return render(request, 'cadastro.html')
        else:
            return render(request, 'cadastro.html')


def login(request):
    context = {}
    if request.method == 'GET':
        logout(request)

        if autenticar(request):
            return render(request, 'cadastro.html')
        else:
            context["erro"] = "Problemas no login."
        return render(request, 'login.html', context)


def autenticar(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    try:
        user = Usuario.objects.get(nome=nome)
        if senha == user.senha:
            return True
        else:
            return False
    except:
        return True

