from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse


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
    if request.method == 'POST':
        nome = request.POST('nome')
        senha = request.POST('senha')

        return render(request, 'login.html')
    else:
        return HttpResponse("Erro ao carregar!")
