from django.urls import path
from . import views

app_name = "sandwiches"

urlpatterns = [
    path("<int:pk>/", views.sandwich_detail, name="detail"),
]
