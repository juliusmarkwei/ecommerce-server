from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps
from .models import CustomUser, SocialProfile, Credentials


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "phone",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
    )

    list_filter = ("email", "username", "is_staff", "is_active")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "phone",
                    "role",
                    "avatar",
                    "locale",
                    "company",
                    "date_joined",
                ),
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
        ("Personal", {"fields": ("bio",)}),
    )


# Registering each model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SocialProfile)
admin.site.register(Credentials)
