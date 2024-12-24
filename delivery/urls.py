from django.urls import path, include
from delivery import views as deliveryviews

urlpatterns = [
    # path('', deliveryviews.home, name='home'),
    path('loginDelivery/',deliveryviews.loginDelivery,name = 'loginDelivery'),
    path('registerDelivery/',deliveryviews.registerDelivery,name = 'registerDelivery'),
    path('home/', deliveryviews.home, name='home'),
]
