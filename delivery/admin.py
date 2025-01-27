from django.contrib import admin
from delivery.models import deliveryUser

class DeliveryUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','phone','email','place']

admin.site.register(deliveryUser, DeliveryUserAdmin)
