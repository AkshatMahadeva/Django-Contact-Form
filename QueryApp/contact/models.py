from email.policy import default
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name