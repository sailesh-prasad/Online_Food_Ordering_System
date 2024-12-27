from rest_framework import serializers
from restaurant.models import Restaurant,Payment,Product,Cart,restaurantUser,foodItems
from customer.models import Place


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class foodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodItems
        fields = '__all__'

class RestaurantUserSerializer(serializers.ModelSerializer):
    # Fields to be included in the serializer
    state = serializers.CharField(source='state.name') 
    city = serializers.CharField(source='city.name') 
    #place = serializers.SerializerMethodField()
    food_items = serializers.SerializerMethodField()
    class Meta:
        model = restaurantUser
        fields = '__all__'

    # Method to count the menu items 
    def get_food_items(self, obj):
        items = obj.food_items.all()
        summary = f"{len(items)} items"
        return summary
    
    # Method to get the place name
    # def get_place(self, obj): 
    #     try: 
    #         place = Place.objects.get(id=obj.place) 
    #         return place.name 
    #     except Place.DoesNotExist: 
    #         return None
      
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'