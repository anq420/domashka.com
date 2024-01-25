from django.db import models


class Comments(models.Model):
    writer_name = models.CharField(max_length=50)
    comment_content = models.TextField()
