from django.db import models

class Ordering(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

# class Comments(models.model):

