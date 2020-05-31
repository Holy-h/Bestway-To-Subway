from django.shortcuts import render
from sandwiches import models as sandwich_models


def home(request):
    fav_sandwiches = sandwich_models.Sandwich.objects.all().order_by("-views")[:5]
    new_sandwiches = sandwich_models.Sandwich.objects.all().order_by("-created")[:5]
    return render(
        request,
        "home.html",
        context={"fav_sandwiches": fav_sandwiches, "new_sandwiches": new_sandwiches},
    )
