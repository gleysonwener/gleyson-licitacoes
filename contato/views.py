from time import sleep
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contato.models import Contatos
from django.core.paginator import Paginator
import datetime

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
            messages.warning(request, 'E-mail já cadastrado, informe um e-mail diferente.')
            return render(request, template_name)

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
    
    ultimos_cadastros = Contatos.objects.filter(data_cadastro__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    
    quantidade_cadastro_total = Contatos.objects.all()
    
    contatos = Contatos.objects.all().order_by('-id')

    contato_paginator = Paginator(contatos, 10)

    page_number = request.GET.get('page')
    page = contato_paginator.get_page(page_number)

    context = {
        'page': page,
        'ultimos_cadastros': ultimos_cadastros,
        'quantidade_cadastro_total': quantidade_cadastro_total,
    }
    return render(request, template_name, context)

