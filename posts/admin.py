from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_at', 'total_likes')
    search_fields = ('author__username', 'content')
    filter_horizontal = ('likes',)



admin.site.register(Comment)