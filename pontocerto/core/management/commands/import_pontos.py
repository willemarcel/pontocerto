# -*- coding: utf-8 -*-

import simplejson

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

from ...models import Ponto


def create_point(feature):
    point = Ponto(osmid=feature.get('id').split('/')[-1],
                    location=Point(feature['geometry'].get('coordinates')))

    if feature['properties'].get('name') is not None:
        point.name = feature['properties'].get('name')

    if feature['properties'].get('ref') is not None:
        point.wheelchair = feature['properties'].get('ref')

    point.save()


def update_point(point, feature):
    if point.nome != feature['properties'].get('name'):
        point.nome = feature['properties'].get('name')

    if point.ref != feature['properties'].get('ref'):
        point.ref = feature['properties'].get('ref')

    if point.location != Point(feature['geometry']['coordinates']):
        point.location = Point(feature['geometry']['coordinates'])

    point.save()


class Command(BaseCommand):
    args = 'filename'
    help = 'Importa ou atualiza pontos de ônibus a partir de um arquivo GeoJSON'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for feature in data['features']:
                if feature['properties'].get('highway') == 'bus_stop' and \
                        feature['geometry'].get('type') == 'Point':
                    try:
                        point = Ponto.objects.get(osmid=
                                            feature.get('id').split('/')[-1])
                        update_point(point, feature)
                    except Ponto.DoesNotExist:
                        create_point(feature)