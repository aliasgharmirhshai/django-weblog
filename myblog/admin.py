from django.contrib import admin
from .models import Post, Comments
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'publish',)
    list_filter = ('status',)
    search_fields = ('body','title',)
    date_hierarchy = 'publish'
    list_editable = ('status',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created',)
    list_filter = ('active', 'created', 'updated',)
    search_fields = ('name', 'body', 'email',)