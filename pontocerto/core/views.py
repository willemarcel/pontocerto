from rest_framework import generics

from .models import Ponto
from .serializers import PontoSerializer


class GeojsonPontoList(generics.ListCreateAPIView):
    model = Ponto
    serializer_class = PontoSerializer