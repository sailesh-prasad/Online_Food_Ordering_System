from rest_framework import serializers
from customer.models import *

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerUserSerializer(serializers.ModelSerializer): 
    # Fields to be included in the serializer
    state = serializers.CharField(source='state.name') 
    city = serializers.CharField(source='city.name') 
    place = serializers.SerializerMethodField()
    orders = serializers.SerializerMethodField()
    
    class Meta: 
        model = customerUser 
        fields = '__all__'

    # Method to count the number of orders made by the customer
    def get_orders(self, obj):
        return obj.orders.count()
    
    # Method to get the place name
    def get_place(self, obj):
        if obj.place.isdigit():
            try:
                place = Place.objects.get(id=int(obj.place))
                return place.name
            except Place.DoesNotExist:
                return None
        else:
            return obj.place
    
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'





