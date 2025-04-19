from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculo.as_view(), name="listar-veiculo")
]