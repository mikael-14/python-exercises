from rest_framework import serializers

from contactos.models import *

class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = ('nome', 'numero', 'morada')