from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from contactos.models import *
from contactos.forms import *

def index(request):
    dic = {
        "msg" : "Hello World",
        "res" : []
    }

    x = Contacto.objects.all()
    for i in x:
        dic['res'].append(
            {
            "nome" : i.nome,
            "numero" : i.numero,
            "morada" : i.morada
            }
        )
    return render(request, "index.html", dic)

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
def criarContacto(request):

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactoForm()

    return render(request,"criarContacto.html",{'form':form})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from contactos.serializer import *

@api_view(['GET'])
def getContactos(request):
    if request.method == 'GET':
        x = Contacto.objects.all()
        s = ContactoSerializer(x,many=True)
        return Response(s.data)