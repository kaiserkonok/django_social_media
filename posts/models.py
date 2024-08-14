from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
   content = models.TextField()
   image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   VISIBILITY_CHOICES = [
     ('public', 'Public'),
     ('private', 'Private'),
     ('draft', 'Draft'),
   ]

   visibility = models.CharField(
     max_length=10,
     choices=VISIBILITY_CHOICES,
     default='public'
   )


   def __str__(self):
      return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
