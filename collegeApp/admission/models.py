from django.db import models

# Create your models here.
class UserLoginDetails(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.email}"