from django.shortcuts import render
from rest_framework import viewsets
from delivery.models import deliveryUser, DeliveryPersonLocation
from delivery.api.serializers import DeliveryUserSerializer, DeliveryPersonLocationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# A viewset for viewing and editing delivery person instances.
# class DeliveryPersonViewSet(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = deliveryUser.objects.all()
#     serializer_class = DeliveryPersonSerializer

# A viewset for viewing and editing delivery user instances.
class DeliveryUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = deliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer

# A viewset for viewing and editing feedback instances.
# class Feedback_dViewSet(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Feedback.objects.all()
#     serializer_class = Feedback_dSerializer

# A viewset for viewing and editing contact instances.
# class Contact_dViewSet(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Contact.objects.all()
#     serializer_class = Contact_dSerializer

# A viewset for viewing and editing delivery person instances.
class DeliveryPersonLocationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DeliveryPersonLocation.objects.all()
    serializer_class = DeliveryPersonLocationSerializer