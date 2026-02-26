from rest_framework.serializers import ModelSerializer

from core.models import Editora

class EditoraSerializer(ModelSerializer):
    class meta:
        model = Editora
        fields = '__all__'