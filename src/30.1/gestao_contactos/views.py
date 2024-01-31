from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from gestao_contactos.models import *

# Create your views here.
def index(request):
    x = Contacto.objects.all()
    return HttpResponse(loader.get_template("index.html").render({"x": x}, request))

from rest_framework.decorators import api_view
from rest_framework.response import Response
from gestao_contactos.serializer import *

@api_view(['GET'])
def getContactos(request):
    if request.method == 'GET':
        x = Contacto.objects.all()
        s = ContactoSerializer(x,many=True)
        return Response(s.data)    