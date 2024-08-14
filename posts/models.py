from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
   content = models.TextField()
   image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
   likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
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


   def total_likes(self):
        return self.likes.count()


   def total_comments(self):
        return self.comments.count()


   def __str__(self):
      return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"