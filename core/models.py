from django.db import models


class ItemModel(models.Model):

    """ ItemModel Model """

    name = models.CharField(max_length=40, unique=True)
    en_name = models.CharField(max_length=100, unique=True, default="")
    calorie = models.IntegerField(verbose_name="칼로리")
    bio = models.TextField(verbose_name="설명", default="", blank=True)
    limited = models.BooleanField(verbose_name="한정판매", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

