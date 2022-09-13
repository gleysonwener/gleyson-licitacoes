from django.urls import path
from . views import novo_contato, lista_contatos

app_name = 'contatos'

urlpatterns = [
    # path('', lista_index, name='lista_index' ),
    path('', novo_contato, name='novo_contato' ),
    path('listagem/', lista_contatos, name='lista_contatos' ),
    # path('listagem/', ContatoListView.as_view(), name='lista_contatos' ),
]
