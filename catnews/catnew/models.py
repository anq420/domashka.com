from django.db import models


class News(models.Model):
    author = models.CharField(max_length=120, null=False, blank=False, default='user')
    image = models.ImageField(upload_to='static/images', blank=True, null=True, default=None)
    title = models.CharField(max_length=128, null=False, blank=False, unique=True)
    content = models.TextField(null=False, blank=False)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}, {self.content}, {self.image}'

    class Meta:
        verbose_name_plural = 'News'


class Comment(models.Model):
    nickname = models.CharField(max_length=128)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments_news')

    def __str__(self):
        return f'{self.nickname}, {self.content}'
