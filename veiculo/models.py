from django.db import models
from datetime import datetime
from veiculo.consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.TextField()
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS) 

