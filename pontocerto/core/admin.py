from django.contrib.gis import admin

from .models import Ponto, Avaliacao


admin.site.register(Ponto, admin.OSMGeoAdmin)
admin.site.register(Avaliacao)