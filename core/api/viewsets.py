from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico

class AccountViewSet(ModelViewSet):
    #pega todos os dados do banco de dados e retorna nesse objeto queryset
    queryset = PontoTuristico.objects.all()
    #como você quer mostrar esses dados
    serializer_class = PontoTuristicoSerializer