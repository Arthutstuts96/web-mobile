from django.contrib import admin

from anuncio.models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['veiculo', 'preco', 'estaAtivo', 'avaliacao']
    # search_fields = ['modelo', ]

admin.site.register(Anuncio, AnuncioAdmin)