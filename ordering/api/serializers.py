from rest_framework import serializers
from ordering.models import  Comment #,Odering

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class OrderingSerializer(serializers.ModelSerializer):
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Ordering
#         fields = '__all__'
