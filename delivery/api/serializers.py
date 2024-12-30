from rest_framework import serializers
from customer.models import Place
from delivery.models import DeliveryPerson,deliveryUser, Feedback, Contact, DeliveryPersonLocation

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'
    

class DeliveryUserSerializer(serializers.ModelSerializer):
    # Fields to be included in the serializer
    state = serializers.CharField(source='state.name') 
    city = serializers.CharField(source='city.name') 
    place = serializers.SerializerMethodField()
    class Meta:
        model = deliveryUser
        fields = '__all__'

    #Method to get the place name    
    def get_place(self, obj):
        if obj.place.isdigit():
            try:
                place = Place.objects.get(id=int(obj.place))
                return place.name
            except Place.DoesNotExist:
                return None
        else:
            return obj.place

class Feedback_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class Contact_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class DeliveryPersonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPersonLocation
        fields = '__all__'