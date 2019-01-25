from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)