from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class List(models.Model):
    user = models.ForeignKey(User, related_name="list_user", on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length = 300)
    completed = models.BooleanField(default=False)
    time_added = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"{self.item} {self.completed}"
