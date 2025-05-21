from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculo.as_view(), name="listar-veiculo"),
    path('novo/', CriarVeiculo.as_view(), name="criar-veiculo"),
    path('<int:pk>/', EditarVeiculos.as_view(), name="editar-veiculos"),  
    path('deletar/<int:pk>/', DeletarVeiculos.as_view(), name="deletar-veiculos"),      
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name="foto-veiculo")
]