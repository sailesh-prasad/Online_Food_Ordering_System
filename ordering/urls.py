"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from customer import views as customerviews
from restaurant import views as restaurantviews
# from menu import views as menuviews
# from order import views as orderviews
from delivery import views as deliveryviews
from . import views
from ordering.views import ChangePasswordView, ResetPasswordView
from .views import forget_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('', include('restaurant.urls')),
    path('', include('delivery.urls')),
    path('api/', include('ordering.api.urls')),
 
    

    # path('loginDelivery/',deliveryviews.loginDelivery,name = 'loginDelivery'),
    # path('registerDelivery/',deliveryviews.registerDelivery,name = 'registerDelivery'),
    # path('home/', deliveryviews.home, name='home'),
    # path('login/', customerviews.loginUser, name='login'),
    # path('track_delivery/<int:order_id>/', deliveryviews.track_delivery, name='track_delivery'),  # Ensure this line is included
    # path('fetch_live_location/', deliveryviews.fetch_live_location, name='fetch_live_location'),
    # path('feedback_form/', deliveryviews.feedback_form, name='feedback_form'),

    # path('loginDelivery/',deliveryviews.loginDelivery,name = 'loginDelivery'),
    # path('registerDelivery/',deliveryviews.registerDelivery,name = 'registerDelivery'),
    # path('home/', deliveryviews.home, name='home'),
    # path('login/', customerviews.loginUser, name='login'),
    path('menu/',views.menu,name = 'menu'),
    path('restaurant/<int:restaurant_id>/menu/', views.restaurant_menu, name='restaurant_menu'),
    path('cart/', views.Cart, name='cart'),
    path('forget_password/', forget_password, name='forget_password'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),
         name='password_reset_complete'),
    path('run-speech-recog/', views.run_speech_recog, name='run_speech_recog'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('search', views.search, name='search'),
    path('filter', views.filter, name ='filter'),
    path('city-autocomplete/', views.city_autocomplete, name='city_autocomplete'),
    # path('track_delivery/', customerviews.track_delivery, name='track_delivery'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

