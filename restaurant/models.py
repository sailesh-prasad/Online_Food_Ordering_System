from django.db import models
class Restaurant(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, default="Unknown Address")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    cuisine_type = models.CharField(max_length=50, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    website_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
