from django.contrib import admin
from contactos.models import *

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nome','numero','morada','idade']

admin.site.register(Contacto,ContactoAdmin)

class LigaContactoAdmin(admin.ModelAdmin):
    list_display = ['origem','destino']
    search_fields = ['origem']

admin.site.register(LigaContacto,LigaContactoAdmin)