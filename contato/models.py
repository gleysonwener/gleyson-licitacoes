from datetime import datetime
import email
from time import timezone
from django.db import models

class Contatos(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('Email')
    telefone = models.PositiveIntegerField('Telefone', blank=True, null=True)
   
    # data = models.DateTimeField(default=timezone)

    def __str__(self):
        return self.nome