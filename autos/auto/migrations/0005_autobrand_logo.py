# Generated by Django 5.0.1 on 2024-01-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_alter_userauto_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='autobrand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Логотип бренда'),
        ),
    ]
