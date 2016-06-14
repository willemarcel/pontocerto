# -*- coding: utf-8 -*-
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer

from .models import Ponto, Avaliacao


class AvaliacaoSerializer(ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = (
            'acesso', 'abrigo', 'piso', 'rampa', 'calcada', 'plataforma',
            'transito', 'equipamento', 'identificacao', 'piso_tatil',
            'linhas', 'logradouro', 'final'
            )


class PontoSerializer(GeoFeatureModelSerializer):
    avaliacao = AvaliacaoSerializer(many=False)

    class Meta:
        model = Ponto
        geo_field = "location"
        fields = ('id', 'nome', 'osmid', 'avaliacao')
