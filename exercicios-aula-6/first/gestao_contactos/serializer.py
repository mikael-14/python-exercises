from rest_framework import serializers
from gestao_contactos.models import *
# Create your models here.

class Contacto(models.Model):
    nome = models.CharField(max_length=100)
    numero_telefone = models.CharField(max_length=100,primary_key=True)
    morada = models.CharField(max_length=100)