from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    """ Custom User Admin"""
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "login_method"
                )
            }
        ),
    )

    list_filter = UserAdmin.list_filter

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "language",
        "currency",
        "email_verified",
        "login_method",
    )