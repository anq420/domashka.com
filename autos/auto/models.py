from django.db import models


class UserAuto(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=25, unique=True)
    car = models.ForeignKey('Auto', max_length=255, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.email} {self.phone_number} {self.car}'


class Auto(models.Model):
    brand = models.ForeignKey('AutoBrand', max_length=255, on_delete=models.CASCADE)
    model = models.ForeignKey('AutoModel', max_length=255, on_delete=models.CASCADE)
    vin_code = models.CharField(max_length=255, unique=True)
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.brand} {self.model} {self.vin_code}'


class AutoModel(models.Model):
    model_name = models.CharField(max_length=255, unique=True)
    count = models.CharField(max_length=255)
    brand = models.ForeignKey('AutoBrand', max_length=255, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model_name}'


class AutoBrand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Логотип бренда")

    def __str__(self):
        return f'{self.name}'
