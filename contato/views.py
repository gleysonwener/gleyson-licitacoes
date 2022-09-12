from django.shortcuts import render, redirect

from contato.models import Contatos


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

