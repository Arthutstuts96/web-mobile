from django.db import models

from veiculo.models import Veiculo

class Anuncio(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    preco = models.DecimalField(decimal_places=2, max_digits=7)
    descricao = models.TextField(max_length=200)
    data = models.DateField(auto_now=True)
    estaAtivo = models.BooleanField(default=True)
    avaliacao = models.DecimalField(decimal_places=1, max_digits=2)
