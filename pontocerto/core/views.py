from rest_framework.generics import ListAPIView

from .models import Ponto
from .serializers import PontoSerializer


class GeojsonPontoList(ListAPIView):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer
