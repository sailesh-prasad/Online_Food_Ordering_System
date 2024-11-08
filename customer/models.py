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


# class Student(models.Model):

#     CLASS_CHOICES = [
#         ('nursery', 'Nursery'),
#         ('lkg', 'LKG'),
#         ('ukg', 'UKG'),
#         ('1st', '1st Class'),
#         ('2nd', '2nd Class'),
#     ]

#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     father_name = models.CharField(max_length=255)
#     mother_name = models.CharField(max_length=255)
#     student_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
#     phone_number = models.CharField(max_length=15)  # Assuming a simple phone number field
#     class_teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
#     address = models.TextField()
#     email = models.EmailField(unique=True)
#     date_of_join = models.CharField(max_length=15)
#     date_of_leaving = models.CharField(max_length=15)
#     second_phone_number = models.CharField(max_length=15, blank=True, null=True)
#     photo = models.ImageField(upload_to='static/images/', blank=True, null=True)
#     identity_marks = models.TextField(blank=True)
#     aadhar_number = models.CharField(max_length=20, blank=True)
#     birth_certificate_number = models.CharField(max_length=20, blank=True)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

