
from django.urls import path
from . import views

urlpatterns = [
    # ...existing code...
    path('restaurant/<int:restaurant_id>/menu/', views.restaurant_menu, name='restaurant_menu'),
]