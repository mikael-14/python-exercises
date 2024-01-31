from django.contrib import admin
from gestao_contactos.models import *
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_telefone', 'morada')
admin.site.register(Contacto, ContactoAdmin)

class LigaContactoAdmin(admin.ModelAdmin):
    list_display = ('origem', 'destino')
admin.site.register(LigaContacto, LigaContactoAdmin)

admin.site.register(LigaContacto)
