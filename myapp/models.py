from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    district_name = models.CharField(max_length=255)
    district_code = models.CharField(null=True, blank=True, max_length=255)
    district_id = models.IntegerField(null=True, blank=True)
    state_name = models.CharField(null=True, blank=True, max_length=255)
    father_name = models.CharField(null=True, blank=True, max_length=255)
    mother_name = models.CharField(null=True, blank=True, max_length=255)
    state_id = models.IntegerField(null=True, blank=True)
    
    age = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.username
