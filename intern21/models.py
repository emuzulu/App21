from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Application(models.Model):
    company = models.CharField(max_length=64)
    role = models.CharField(max_length=64)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")