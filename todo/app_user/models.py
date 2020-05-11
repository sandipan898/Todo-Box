from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class AppUser(models.Model):
    first_name = models.OneToOneField(User, related_name="f_name", max_length=30, on_delete=models.CASCADE)
    last_name = models.OneToOneField(User, related_name="l_name", max_length=30, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        