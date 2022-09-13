from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contato.models import Contatos
from django.core.paginator import Paginator


def novo_contato(request):
    template_name = 'index.html'

    if request.method == 'GET':
        return render(request, template_name)
    
    elif request.method =='POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        contato = Contatos.objects.filter(email=email)

        if contato.exists():
            pass
        
        contatos = Contatos(
            nome = nome,
            email = email,
            telefone = telefone
        )

        contatos.save()

        return render(request, template_name)

@login_required
def lista_contatos(request):
    template_name = 'contato/principal.html'
    contatos = Contatos.objects.all()

    contato_paginator = Paginator(contatos, 10)

    page_number = request.GET.get('page')
    page = contato_paginator.get_page(page_number)

    context = {
        'page': page,
    }
    return render(request, template_name, context)

