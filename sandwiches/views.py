from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import models


def sandwich_detail(request, pk):
    # get_object_or_404
    # 해당 모델로 부터 값을 가져오되 값이 존재하지 않는 경우 404page로 리다이렉트함
    # 커스텀 -> 404.html
    sandwich = get_object_or_404(models.Sandwich, pk=pk)
    return render(request, "detail.html", context={"sandwich": sandwich})
