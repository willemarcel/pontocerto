# -*- coding: utf-8 -*-
from djgeojson.views import GeoJSONLayerView

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .models import Ponto


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Ponto,
                                                    geometry_field='location'),
                            name='data'),
)