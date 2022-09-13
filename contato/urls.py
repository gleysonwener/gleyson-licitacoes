from django.urls import path
from . views import novo_contato, lista_contatos, ListaContatosPdfView

app_name = 'contatos'

urlpatterns = [
    path('', novo_contato, name='novo_contato' ),
    path('listagem/', lista_contatos, name='lista_contatos' ),
    path('listagem_pdf/', ListaContatosPdfView.as_view(), name='lista_contatos_pdf' ),
]
