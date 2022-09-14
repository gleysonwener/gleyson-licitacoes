from datetime import datetime
from . manages import ContatoManager
from time import timezone
from django.db import models

class Contatos(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=16)
    data_cadastro = models.DateTimeField('Cadastraado em:', auto_now=True)
   
    
    objects = ContatoManager()

    def __str__(self):
        return self.nome

