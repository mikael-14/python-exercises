from django.db import models
from django.forms import ModelForm
from contactos.models import *

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nome', 'numero', 'morada', 'idade']

