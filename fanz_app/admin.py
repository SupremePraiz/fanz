from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Like, Message


admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Message)
