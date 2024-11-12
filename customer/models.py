from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User  # Assuming User model is used for customers

class DeliveryPerson(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Customer who wrote the comment
    comment_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user}"


