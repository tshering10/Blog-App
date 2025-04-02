from django.contrib import admin
from posts.models import Post, Comment, Like
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    
admin.site.register(Comment)
admin.site.register(Like)