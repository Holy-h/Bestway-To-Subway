from django.db import models
from django.shortcuts import reverse
from core import models as core_models


class Menu(core_models.ItemModel):

    CATEGORY_CLASSIC = "classic"
    CATEGORY_FRESHNLIGHT = "fresh_and_light"
    CATEGORY_PRIMIUM = "premium"

    CATEGORY_CHOICES = (
        (CATEGORY_CLASSIC, "클래식"),
        (CATEGORY_FRESHNLIGHT, "프레쉬 & 라이트"),
        (CATEGORY_PRIMIUM, "프리미엄"),
    )

    categories = models.CharField(
        choices=CATEGORY_CHOICES, default=CATEGORY_CLASSIC, max_length=20
    )
    ingredient = models.CharField(verbose_name="속재료", max_length=40, default="")
    price = models.IntegerField(verbose_name="가격", default=0)
    photo = models.ImageField(
        verbose_name="이미지", upload_to="images/menus", null=True, blank=True
    )


class Bread(core_models.ItemModel):
    photo = models.ImageField(
        verbose_name="이미지", upload_to="images/breads", null=True, blank=True
    )


class Cheese(core_models.ItemModel):
    photo = models.ImageField(
        verbose_name="이미지", upload_to="images/cheeses", null=True, blank=True
    )


class Sauce(core_models.ItemModel):
    CATEGORY_SAVORY = "savory"
    CATEGORY_SWEET = "sweet"
    CATEGORY_SPICY = "spicy"
    CATEGORY_SOUR = "sour"
    CATEGORY_OTHER = "other"
    CATEGORY_CHOICES = (
        (CATEGORY_SAVORY, "고소한 소스"),
        (CATEGORY_SWEET, "달콤한 소스"),
        (CATEGORY_SPICY, "매콤한 소스"),
        (CATEGORY_SOUR, "새콤한 소스"),
        (CATEGORY_OTHER, "기타"),
    )
    categories = models.CharField(
        choices=CATEGORY_CHOICES, default=CATEGORY_OTHER, max_length=40
    )
    photo = models.ImageField(
        verbose_name="이미지", upload_to="images/sauces", null=True, blank=True
    )


class Sandwich(models.Model):
    menu = models.ForeignKey(
        "Menu",
        verbose_name="메뉴",
        related_name="sandwiches",
        on_delete=models.SET_NULL,
        null=True,
    )
    bread = models.ForeignKey(
        "Bread",
        verbose_name="빵",
        related_name="sandwiches",
        on_delete=models.SET_NULL,
        null=True,
    )
    sauces = models.ManyToManyField("Sauce", verbose_name="소스")
    cheeses = models.ManyToManyField("Cheese", verbose_name="치즈")
    views = models.IntegerField(verbose_name="조회수", blank=True, default=0)
    orders = models.IntegerField(verbose_name="주문수", blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("sandwiches:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.menu}-{self.bread}"

    def get_total_calories(self):
        menu = self.menu
        bread = self.bread
        sauces = self.sauces.all()
        sauces_cal = sum([s.calorie for s in sauces])

        cheeses = self.cheeses.all()
        cheeses_cal = sum([c.calorie for c in cheeses])

        return f"{menu.calorie + bread.calorie + sauces_cal + cheeses_cal}kcal"
