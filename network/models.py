from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add any additional fields or methods here
    pass


class Post(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp}"
