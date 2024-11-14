from django.db import models

class Customer(models.Model):
    # No need to define the 'id' field explicitly, Django will add it automatically
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name