from django.urls import path
from . views import novo_contato

app_name = 'contatos'

urlpatterns = [
    # path('', lista_index, name='lista_index' ),
    path('', novo_contato, name='novo_contato' ),
]
