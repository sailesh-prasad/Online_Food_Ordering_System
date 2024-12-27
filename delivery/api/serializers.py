from rest_framework import serializers
from delivery.models import DeliveryPerson,deliveryUser, Feedback, Contact
from customer.models import Place

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'
    

class DeliveryUserSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='state.name', read_only=True) 
    city = serializers.CharField(source='city.name', read_only=True) 
    place = serializers.SerializerMethodField()
    class Meta:
        model = deliveryUser
        fields = '__all__'
    def get_place(self, obj): 
        try: # Assuming 'place' field contains the place ID 
            place = Place.objects.get(id=obj.place) 
            return place.name 
        except Place.DoesNotExist: 
            return None

class Feedback_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class Contact_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

