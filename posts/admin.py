from django.contrib import admin
from .models import Post, PostImage, Like, Comment, Story

# Register your models here.

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Story)