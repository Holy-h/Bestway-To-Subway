from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Sandwich)
class SandwichAdmin(admin.ModelAdmin):

    list_display = (
        "menu",
        "bread",
        "get_cheeses",
        "get_sauces",
        "get_total_calories",
        "views",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "menu",
                    "bread",
                    "cheeses",
                    "sauces",
                    "views",
                    "orders",
                    "created",
                    "updated",
                ),
            },
        ),
    )
    readonly_fields = ("orders", "created", "updated")

    def get_sauces(self, obj):
        return ", ".join([s.name for s in obj.sauces.all()])

    get_sauces.short_description = "소스"

    def get_cheeses(self, obj):
        return ", ".join([c.name for c in obj.cheeses.all()])

    get_cheeses.short_description = "치즈"


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "categories", "calorie", "price", "get_thumbnail")

    ordering = (
        "categories",
        "name",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "categories",
                    "photo",
                    "name",
                    "en_name",
                    "calorie",
                    "bio",
                    "ingredient",
                    "price",
                    "limited",
                ),
            },
        ),
    )

    def get_thumbnail(self, obj):
        if obj.photo:
            # print(dir(obj.photo))
            return mark_safe(f"<img style='height: 60px;' src='{obj.photo.url}' />")

    get_thumbnail.short_description = "이미지"


@admin.register(models.Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ("name", "en_name", "calorie", "get_thumbnail")

    ordering = ("name",)

    def get_thumbnail(self, obj):
        if obj.photo:
            # print(dir(obj.photo))
            return mark_safe(f"<img style='height: 60px;' src='{obj.photo.url}' />")

    get_thumbnail.short_description = "이미지"


@admin.register(models.Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ("name", "en_name", "calorie", "get_thumbnail")

    ordering = ("name",)

    def get_thumbnail(self, obj):
        if obj.photo:
            # print(dir(obj.photo))
            return mark_safe(f"<img style='height: 60px;' src='{obj.photo.url}' />")

    get_thumbnail.short_description = "이미지"


@admin.register(models.Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ("name", "en_name", "categories", "calorie", "limited")

    ordering = (
        "categories",
        "name",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "categories",
                    "name",
                    "photo",
                    "en_name",
                    "calorie",
                    "bio",
                    "limited",
                ),
            },
        ),
    )
