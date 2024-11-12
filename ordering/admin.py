from django.contrib import admin
from customer.models import Customer
# admin.site.site_header = 'My Awesome Admin'
admin.site.register(Customer)