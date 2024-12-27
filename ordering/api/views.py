from django.shortcuts import render
from rest_framework import viewsets
from ordering.models import  Comment ,Feedback
from .serializers import  CommentSerializer ,FeedbackSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# A viewset for viewing and editing comment instances.
class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# A viewset for viewing and editing feedback instances.
class FeedbackViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

