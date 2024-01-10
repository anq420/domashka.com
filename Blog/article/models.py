from django.db import models
from author.models import Author
from comments.models import Comments


class Article(models.Model):
    article_name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    article_content = models.TextField()
    comments = models.ManyToManyField(Comments)
