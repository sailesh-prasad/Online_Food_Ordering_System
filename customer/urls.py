from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryPersonViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'delivery-persons', DeliveryPersonViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
