from django.contrib import admin
from auto.models import Auto, AutoModel, AutoBrand, UserAuto


class AutoModelInline(admin.TabularInline):
    model = AutoModel


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'vin_code', 'in_use')
    search_fields = ('vin_code', )
    list_filter = ('in_use', 'brand')


@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'count')
    list_filter = ('brand', 'model_name')
    ordering = ('brand', 'model_name')


@admin.register(AutoBrand)
class AutoBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    list_filter = ('name', )
    ordering = ('name', )
    inlines = [AutoModelInline]


@admin.register(UserAuto)
class UserAutoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'phone_number', 'car')
    search_fields = ('first_name', 'second_name', 'email', 'phone_number')
