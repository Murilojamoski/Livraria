from rest_framework.routers import DefaultRouter
from uploader.views import ImageViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='images')
