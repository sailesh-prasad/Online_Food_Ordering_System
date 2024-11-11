from django.db import models
from datetime import date, timedelta
from django.db import models	
from django.contrib.auth.models import User

class Customer(models.Model):
	CustomerId    = models.AutoField(primary_key=True)
	CustomerFName  = models.CharField(max_length=30)
	CustomerLName  = models.CharField(max_length=30)
	CustomerCont  = models.CharField(max_length=10)
	CustomerEmail = models.CharField(max_length=50)
	CustomerPass  = models.CharField(max_length=60)
	Address  = models.CharField(max_length=150,default='')

class Food(models.Model):
	FoodId    = models.AutoField(primary_key=True)
	FoodName  = models.CharField(max_length=30)
	FoodCat   = models.CharField(max_length=30)
	FoodPrice = models.FloatField(max_length=15)
	FoodImage = models.ImageField(upload_to='media',default='')
     
class AdminPrivilege(models.Model):
    AdminId   = models.CharField(primary_key=True,max_length=20)
    AdminPass = models.CharField(max_length=60)

class Cart(models.Model):
	CartId    = models.AutoField(primary_key=True)
	CustEmail = models.CharField(max_length=50)
	FoodId    = models.CharField(max_length=50)
	FoodQuant = models.CharField(max_length=10)

class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.food_item} for {self.customer_name}"



