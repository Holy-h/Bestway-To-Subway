from django.contrib import admin
from . import models


@admin.register(models.Sandwich)
class SandwichAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ("name", "en_name", "calorie")

    ordering = ("name",)


@admin.register(models.Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ("name", "en_name", "calorie")

    ordering = ("name",)


@admin.register(models.Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ("name", "en_name", "calorie", "limited")

    ordering = ("name",)
