from rest_framework.viewsets import ModelViewSet
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
