from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste':123})
    #PARA O POST
    def create(self, request, *args, **kwargs):
        pass
    #PARA DELETE
    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass
    def partial_update(self, request, *args, **kwargs):
        pass

    #funções personalizadas
    #decorator (tem que passar em quais métodos você quer que funcione e detail para pegar a pk
    @action(methods=['get'], detail=True)
    def denunciar(self,request, pk=None):
        pass

    #@action(methods=['get'], detail=False)
    #def teste(self, request):
    #  pass