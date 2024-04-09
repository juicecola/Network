from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField(
        'self', related_name='following_users', symmetrical=False)
    following = models.ManyToManyField(
        'self', related_name='followers_users', symmetrical=False)
    # Other fields and methods

    def follow(self, user):
        """
        Follow another user.
        """
        if not self.is_following(user):
            self.following.add(user)

    def unfollow(self, user):
        """
        Unfollow another user.
        """
        if self.is_following(user):
            self.following.remove(user)

    def is_following(self, user):
        """
        Check if the user is following another user.
        """
        return self.following.filter(id=user.id).exists()


class Post(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp}"
