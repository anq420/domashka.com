# Generated by Django 5.0.1 on 2024-02-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catnew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='author',
            field=models.CharField(default='user', max_length=120),
        ),
    ]
