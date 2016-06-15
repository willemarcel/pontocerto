# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Ponto

User = get_user_model()


class TestCreatePoint(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')
        self.data = {'lat': 0.231, 'lon': 0.345}

    def test_create_point(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('core:create-point'), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ponto.objects.count(), 1)
