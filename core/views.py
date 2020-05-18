from django.shortcuts import render
from sandwiches import models as sandwich_models


def home(request):
    fav_sandwiches = sandwich_models.Sandwich.objects.all().order_by("-views")[:5]
    for sandwich in fav_sandwiches:
        # print(sandwich.menu.photo)
        print(sandwich.sauces.all())
    return render(request, "home.html", context={"fav_sandwiches": fav_sandwiches})
