from django.urls import path, include
from delivery import views as deliveryviews

urlpatterns = [
    path('', deliveryviews.home, name='home'),
]
