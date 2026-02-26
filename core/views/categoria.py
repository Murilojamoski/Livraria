from rest_framework.viewsets import ModelViewSet 

from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objetos.all()
    serializer_class = CategoriaSerializer