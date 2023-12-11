import email
from email import message
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class contact_table(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.name

class reg_table(models.Model):
    email_id=models.EmailField()
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

    def __str__ (self):
        return self.user_name

class add_user(models.Model):
    name=models.CharField(max_length=20)
    email_id=models.EmailField()
    group=models.CharField(max_length=20)

    def __str__(self):
        return self.name


