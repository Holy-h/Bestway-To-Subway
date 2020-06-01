from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import models


def sandwich_detail(request, pk):
    # get_object_or_404
    # 해당 모델로 부터 값을 가져오되 값이 존재하지 않는 경우 404page로 리다이렉트함
    # 커스텀 -> 404.html
    sandwich = get_object_or_404(models.Sandwich, pk=pk)
    same_menu_sandwiches = (
        models.Sandwich.objects.all().filter(menu=sandwich.menu).exclude(pk=pk)[:5]
    )
    other_sandwiches = models.Sandwich.objects.all().order_by("?")[:5]

    # print(other_sandwiches)
    return render(
        request,
        "detail.html",
        context={
            "sandwich": sandwich,
            "same_menu_sandwiches": same_menu_sandwiches,
            "other_sandwiches": other_sandwiches,
        },
    )


def sandwich_order(request, pk):
    sandwich = get_object_or_404(models.Sandwich, pk=pk)
    sandwich.orders += 1
    sandwich.save()
    return redirect(reverse("sandwiches:detail", kwargs={"pk": pk}))
