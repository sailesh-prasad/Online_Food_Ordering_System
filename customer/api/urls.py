# customer/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryPersonViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'delivery-person', DeliveryPersonViewSet, basename='deliveryperson')
router.register(r'comments', CommentViewSet, basename='comment')

# Ensure urlpatterns is defined and includes the router URLs
urlpatterns = [
    path('', include(router.urls)),
]

