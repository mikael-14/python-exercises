from rest_framework import serializers

from gestao_contactos.models import *

class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = ('nome', 'numero_telefone', 'morada')