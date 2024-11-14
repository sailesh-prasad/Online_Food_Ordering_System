from django.urls import path, include
from .api import urls as api_urls

urlpatterns = [
    path('api/', include(api_urls)),  # Include Customer API URLs
    # Add other customer-specific URLs here if needed
]
