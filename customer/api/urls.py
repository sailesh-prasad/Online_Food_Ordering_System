from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet,RestaurantViewSet
# urlpatterns = [
#     path('student_list', views.student_list, name='student_list'),
#     path('studentr-detail/<int:student_id>/', views.student_detail, name='student_detail') 
# ]

router = DefaultRouter()
router.register(r'customer',CustomerViewSet)
router.register(r'restaurant',RestaurantViewSet)

urlpatterns = [
    path('api/',include(router.urls))
]