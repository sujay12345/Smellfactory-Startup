from django.contrib import admin
from .models import User, Post, addcomment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(addcomment)