from django.db import models


class Users(models.Model):
    def __str__(self):
        return self.email

    nickname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
