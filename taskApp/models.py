from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} -- {self.id}"