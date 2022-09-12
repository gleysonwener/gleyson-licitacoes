from datetime import datetime
import email
from time import timezone
from django.db import models

class Contatos(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=16)
   
    # data = models.DateTimeField(default=timezone)

    def __str__(self):
        return self.nome