# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import GeojsonPontoList


urlpatterns = patterns('',
    url(r'^pontos.geojson/$', GeojsonPontoList.as_view(),
         name='api_geojson_ponto_list'),
)