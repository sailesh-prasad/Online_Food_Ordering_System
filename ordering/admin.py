from django.contrib import admin
from customer.models import DeliveryPerson, Feedback

admin.site.register(DeliveryPerson)
admin.site.register(Feedback)

from .models import FoodItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username', 'customer__email')
    inlines = [OrderItemInline] 

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name', 'description')
    list_filter = ('price',)

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
