from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Chamado
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "core/home.html" ) 

#@login_required
def novoChamado(request):
    if request.method == "POST":
        laboratorio = request.POST.get('laboratorio')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')

        print("chegou um post")
        print(f"Laboratório: {laboratorio}, Descrição: {problema}")

        Chamado.objects.create(laboratorio=laboratorio, problema=problema, prioridade=prioridade)
        
       
        return redirect('/listar')

    if request.method == "GET":
        print("chegou um get")
        return render(request, 'core/novo_chamado.html')

# Ainda retorna HttpResponse
def fechar_chamado(request, id):
    chamado = Chamado.objects.get(id=id)
    chamado.delete()
    print(f"Fechando chamado {chamado.id} - {chamado.problema}")
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/listar'>Voltar</a>")

#@login_required
def listar(request):
    # Busca TODOS os registros do banco de dados
    chamados = Chamado.objects.all() 
    return render(request, 'core/listar.html', {"chamados": chamados})
