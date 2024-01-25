from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=100)
