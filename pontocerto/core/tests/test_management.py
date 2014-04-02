from django.test import TestCase
from django.core import management
from django.contrib.gis.geos import Point

from ..models import Ponto


class CommandsTest(TestCase):

    def setUp(self):
        data_test1 = 'media/test_data/ponto1.geojson'
        management.call_command('import_pontos', data_test1)

    def test_import_pontos(self):
        self.assertEqual(Ponto.objects.all().count(), 1)
        self.assertEqual(Ponto.objects.get(osmid=565442609).location,
                        Point(-38.5297511999999998, -13.0038570999999994))
        self.assertEqual(Ponto.objects.get(osmid=565442609).nome, '')
        self.assertEqual(Ponto.objects.get(osmid=565442609).ref, '')

    def test_update_pontos(self):
        data_test2 = 'media/test_data/ponto2.geojson'
        management.call_command('import_pontos', data_test2)

        self.assertEqual(Ponto.objects.get(osmid=565442609).location,
                        Point(-38.5292431000000022, -13.0037538999999995))
        self.assertEqual(Ponto.objects.get(osmid=565442609).nome, 'Rodoviária')
        self.assertEqual(Ponto.objects.get(osmid=565442609).ref, '12345')