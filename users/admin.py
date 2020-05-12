from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    pass
