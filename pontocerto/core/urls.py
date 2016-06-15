# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import GeojsonPontoList, CreatePointView

urlpatterns = [
    url(r'^pontos.geojson/$',
        GeojsonPontoList.as_view(),
        name='api_geojson_ponto_list'),
    url(r'^novo-ponto/$',
        login_required(CreatePointView.as_view()),
        name='create-point'),
    ]
