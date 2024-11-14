from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from restaurant.models import Restaurant
from .serializers import  RestaurantSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
