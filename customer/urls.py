# customer/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('customer.api.urls')),  # Include the api sub-urls
]
