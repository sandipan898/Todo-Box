from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length = 300)
    completed = models.BooleanField(default=False)
    time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item} {self.completed}"