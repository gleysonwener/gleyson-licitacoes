from django.forms import ModelForm
from .models import Contatos
from django import forms


class FormContato(ModelForm):
    class Meta:
        model = Contatos
        exclude = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})