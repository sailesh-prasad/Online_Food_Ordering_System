from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet


router = DefaultRouter()
router.register(r'',RestaurantViewSet)

urlpatterns = [
    path('api/',include(router.urls))
]