from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    upvoted_posts = models.ManyToManyField("Post", blank=True, related_name="likers")



class Post(models.Model):
    content = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)
    postcreator = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts_created")


class addcomment(models.Model):
    user = models.CharField(max_length=64)
    commentcontent = models.CharField(max_length=128)
    forumid = models.PositiveIntegerField()

    