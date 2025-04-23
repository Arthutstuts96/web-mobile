from django.shortcuts import render
from django.views.generic import ListView

from veiculo.models import Veiculo

class ListarVeiculo(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/lista.html'
