from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.apps import apps
from .models import Categories, Products, Reviews


class CategoriesModelAdmin(ModelAdmin):
    list_display = ["id", "name", "tags", "created_at", "updated_at"]
    search_fields = ["name", "tags"]


class ProductsModelAdmin(ModelAdmin):
    list_display = [
        "id",
        "category",
        "title",
        "picture",
        "price",
        "discount_type",
        "tags",
        "created_at",
        "updated_at",
    ]
    search_fields = ["category", "title", "price", "discount_type", "tags"]


class ReviewModelAdmin(ModelAdmin):
    list_display = ["id", "user_id", "product", "comments", "created_at"]


admin.site.register(Categories, CategoriesModelAdmin)
admin.site.register(Products, ProductsModelAdmin)
admin.site.register(Reviews, ReviewModelAdmin)
