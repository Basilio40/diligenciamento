from django.db import models
from cadastro import models as cadastro_models


# Create your models here.
class Proposta(models.Model):
    cliente = models.ForeignKey(cadastro_models.Cliente, on_delete=models.CASCADE)

    

class ServicoProposta(models.Model):
    servico = models.ForeignKey(cadastro_models.Servico, on_delete=models.CASCADE)
    valor_servico = models.DecimalField(max_digits=19,decimal_places=3, null=True, blank=True)
    Valor_deslocamento = models.CharField(max_length=100, null=True, blank=True)
    cliente =models.ForeignKey(Proposta, on_delete= models.CASCADE)

    class Meta:
        verbose_name = "Proposta de Serviço"
        verbose_name_plural = "Propostas de Serviço"