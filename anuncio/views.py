from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from anuncio.models import Anuncio

class ListarAnuncios(ListView):
    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'
