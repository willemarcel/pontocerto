from rest_framework.generics import ListAPIView

from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point
from django.forms import Form, CharField, FloatField
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Ponto
from .serializers import PontoSerializer


class GeojsonPontoList(ListAPIView):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer


class PointForm(Form):
    nome = CharField(max_length=100, required=False)
    lat = FloatField(label="Latitude")
    lon = FloatField(label="Longitude")


class CreatePointView(FormView):
    template_name = 'core/create_point.html'
    form_class = PointForm

    def form_valid(self, form):
        ponto = Ponto.objects.create(
            nome=form.cleaned_data.get('nome'),
            location=Point(
                form.cleaned_data.get('lon'),
                form.cleaned_data.get('lat')
                )
            )
        url = reverse(
            'admin:{0}_{1}_change'.format(
                ponto._meta.app_label, ponto._meta.model_name
                ), args=(ponto.pk,)
            )
        return HttpResponseRedirect(url)
