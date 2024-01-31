from django.db import models
 
# Create your models here.
 
class Contacto(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=100, primary_key = True)
    morada = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    
    def __str__(self):
        return self.numero


class LigaContacto(models.Model):
    class Meta:
        unique_together = (('origem', 'destino'))
 
    origem = models.ForeignKey(Contacto,on_delete=models.CASCADE,related_name='%(class)s_origem')
    destino = models.ForeignKey(Contacto,on_delete=models.CASCADE,related_name='%(class)s_destino')

#    def __str__(self):
#        return self.origem + ":" + self.destino