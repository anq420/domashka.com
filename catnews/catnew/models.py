from django.db import models


class New(models.Model):
    author = models.CharField(max_length=120, null=False, blank=False, default='user')
    image = models.ImageField(upload_to='static/images/', blank=True)
    title = models.CharField(max_length=128, null=False, blank=False, unique=True)
    content = models.TextField(null=False, blank=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.content}, {self.image}'


class Comment(models.Model):
    nickname = models.CharField(max_length=128)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    news = models.ForeignKey('New', on_delete=models.CASCADE, related_name='comments_news')

    def __str__(self):
        return f'{self.nickname}, {self.content}'
