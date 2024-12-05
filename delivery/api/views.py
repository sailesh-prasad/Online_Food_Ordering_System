from django.shortcuts import render
from rest_framework import viewsets
from delivery.models import DeliveryPerson
from .serializers import DeliveryPersonSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer
