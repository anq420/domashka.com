from django.contrib import admin
from catnew.models import New, Comment


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'likes', 'dislikes', 'rating', 'date', 'views', 'comment')
    search_fields = ('title', 'content')
    ordering = ('rating', 'views')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'date', 'content', 'likes', 'dislikes')
