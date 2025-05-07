from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculo.as_view(), name="listar-veiculo"),
    path('cadastrar/', CadastrarVeiculo.as_view(), name="cadastrar-veiculo"),
]