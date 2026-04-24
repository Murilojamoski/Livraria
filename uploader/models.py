from django.db import models
from cloudinary.models import CloudinaryField


class Image(models.Model):
    attachment_key = models.CharField(max_length=255, unique=True)
    arquivo = CloudinaryField('image', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.attachment_key}'
