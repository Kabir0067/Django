from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'user', 'created_on', 'location', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_on', 'user', 'location')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_on')
    search_fields = ('body', 'name', 'email')
    list_filter = ('created_on', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
