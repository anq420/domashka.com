# Generated by Django 5.0.1 on 2024-02-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catnew', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
