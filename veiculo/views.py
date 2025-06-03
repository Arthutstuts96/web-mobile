from django.http import FileResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from veiculo.serializers import SerializadorVeiculo
from veiculo.forms import FormularioVeiculo
from veiculo.models import Veiculo

class ListarVeiculo(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculo(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/cadastrar.html'
    success_url = reverse_lazy('listar-veiculo')

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404('Foto não encontrada ou não autorizado')
        except Exception as e:
            raise e
class EditarVeiculos(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    success_url = reverse_lazy('listar-veiculo')
    template_name = 'veiculo/editar.html'
class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    model = Veiculo
    success_url = reverse_lazy('listar-veiculo')    
    template_name = 'veiculo/deletar.html'
class APIListarVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()