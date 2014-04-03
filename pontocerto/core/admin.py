from django.contrib.gis import admin

from .models import Ponto, Avaliacao


class PontoAdmin(admin.OSMGeoAdmin):
    search_fields = ['id', 'osmid', 'nome']
    list_display = ('__unicode__', 'osmid', 'nome')

admin.site.register(Ponto, PontoAdmin)
admin.site.register(Avaliacao)