from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_num = models.IntegerField(null =True)
    email = models.EmailField(max_length=50)
