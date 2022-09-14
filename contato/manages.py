from django.db import models
from django.db.models import Q

class ContatoManager(models.Manager):

    def busca(self, termo=None):
        qs = self.get_queryset()
        if termo is not None :
            or_lookup = (Q(nome__icontains=termo) | Q(email__icontains=termo) | Q(telefone__icontains=termo) | Q(data_cadastro__icontains=termo))
        qs = qs.filter(or_lookup).distinct()
        return qs