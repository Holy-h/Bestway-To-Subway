from django.contrib import admin
from . import models


@admin.register(models.Sandwich)
class SandwichAdmin(admin.ModelAdmin):

    list_display = ("menu", "bread", "get_cheeses", "get_sauces", "get_total_calories")

    fieldsets = (
        (None, {"fields": ("menu", "bread", "cheese", "sauce", "views", "orders"),}),
    )
    readonly_fields = ("views", "orders")

    def get_sauces(self, obj):
        return ", ".join([s.name for s in obj.sauce.all()])

    get_sauces.short_description = "소스"

    def get_cheeses(self, obj):
        return ", ".join([c.name for c in obj.cheese.all()])

    get_cheeses.short_description = "치즈"


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "categories", "en_name", "calorie", "price", "limited")

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
                    "en_name",
                    "calorie",
                    "bio",
                    "limited",
                ),
            },
        ),
    )
