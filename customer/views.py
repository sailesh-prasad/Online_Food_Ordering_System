from rest_framework import viewsets
from .models import DeliveryPerson, Comment
from .serializers import DeliveryPersonSerializer, CommentSerializer

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

