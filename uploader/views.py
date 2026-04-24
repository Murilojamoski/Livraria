from rest_framework.viewsets import ModelViewSet
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'attachment_key'
