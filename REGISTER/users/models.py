from django.db import models


class Users(models.Model):
    def __str__(self):
        return self.email

    nickname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
