from django.db import models
from core import models as core_models


class Menu(core_models.ItemModel):
    pass


class Bread(core_models.ItemModel):
    pass


class Cheese(core_models.ItemModel):
    pass


class Sauce(core_models.ItemModel):
    pass


class Sandwich(models.Model):
    bread = models.ForeignKey(
        "Bread", related_name="sandwiches", on_delete=models.SET_NULL, null=True
    )
    sauce = models.ManyToManyField("Sauce")
    cheese = models.ManyToManyField("Cheese")

    # def get_total_calories(self):
    #   bread_cal = self.bread.calorie
    #   sauce = self.
