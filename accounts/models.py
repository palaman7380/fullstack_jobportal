from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLL_CHOICES = [
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
    ]
    roll = models.CharField(max_length=20, choices=ROLL_CHOICES, default='jobseeker')


    def __str__(self):
        return self.username