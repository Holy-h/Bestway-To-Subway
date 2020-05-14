from datetime import datetime
from django.shortcuts import render


def home(request):
    now = datetime.now()
    isHungry = True
    return render(request, "home.html", context={"now": now, "isHungry": isHungry})
