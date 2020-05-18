from django.shortcuts import render
from . import models


def detail(request, pk):
    print(pk)
    sandwich = models.Sandwich.objects.get(pk=pk)
    print(sandwich)
    return render(request, "detail.html", context={"sandwich": sandwich})
