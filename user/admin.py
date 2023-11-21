from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps
from .models import CustomUser, SocialProfile, Credentials


class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "phone",
        "first_name",
        "last_name",
        "is_active",
        "created_at",
    ]
    # exclude = ["date_joined"]

    list_filter = ["email", "username", "is_staff", "is_active"]


# Registering each model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SocialProfile)
admin.site.register(Credentials)
