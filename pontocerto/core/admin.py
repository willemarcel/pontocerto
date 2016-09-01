from django.contrib.gis import admin

from .models import Ponto, Avaliacao


class PontoAdmin(admin.OSMGeoAdmin):
    search_fields = ['id', 'osmid', 'nome']
    list_display = ('__str__', 'osmid', 'nome')


class AvaliacaoAdmin(admin.OSMGeoAdmin):
    search_fields = ['ponto__id', 'ponto__nome']
    list_display = ['id', 'ponto', 'final']


admin.site.register(Ponto, PontoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
