
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contato.models import Contatos
from django.core.paginator import Paginator
import datetime
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.list import ListView
from contato.utils import GeraPDFMixin
from django.db.models import Q

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

# relatórios pdf
@method_decorator(login_required, name='dispatch')
class ListaContatosPdfView(View, GeraPDFMixin):

    def get(self, request, *args, **kwargs):
        contatos = Contatos.objects.all()

        contexto = {
            'contatos': contatos,
            'quant_contatos': contatos.count(),
        }
        pdf = GeraPDFMixin()
        return pdf.render_to_pdf('contato/contatospdf.html', contexto)


@login_required
def buscar(request):
    template_name = 'contato/busca_resultados.html'
    context = {}
    termo = request.GET.get('termo', None)

    if termo is not None:
        contatos = Contatos.objects.busca(termo=termo)
        
        context['contatos'] = contatos

    return render(request, template_name, context)
