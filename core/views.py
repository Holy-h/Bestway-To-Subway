from django.shortcuts import render
from sandwiches import models as sandwich_models


def home(request):
    all_sandwiches = sandwich_models.Sandwich.objects.all()
    for sandwich in all_sandwiches:
        print(sandwich.menu.photo)
    return render(request, "home.html", context={"all_sandwiches": all_sandwiches})
