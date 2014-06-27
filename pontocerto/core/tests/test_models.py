# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.gis.geos import Point

from ..models import Ponto


class CreatePontoTest(TestCase):

    def setUp(self):
        ponto = Ponto(osmid=123, location=Point(1.34, 2.45))
        ponto.save()

    def test_unicode(self):
        self.assertEqual(Ponto.objects.get(osmid=123).__str__(),
                            str(Ponto.objects.get(osmid=123).id))