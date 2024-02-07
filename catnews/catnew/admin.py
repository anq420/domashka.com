from django.contrib import admin
from catnew.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'likes', 'dislikes', 'rating', 'created_at', 'views')
    search_fields = ('title', 'content')
    ordering = ('rating', 'views')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'date', 'content', 'likes', 'dislikes')
