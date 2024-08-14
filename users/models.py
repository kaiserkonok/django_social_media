from django.db import models
from django.contrib.auth.models import User
from .choices import COUNTRY_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=2, choices=COUNTRY_CHOICES, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
