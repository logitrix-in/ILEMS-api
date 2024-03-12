from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    police_station = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    profile_created = models.DateTimeField(auto_now_add=True)
    profile_created_by = models.CharField(max_length=255, blank=True, null=True)
