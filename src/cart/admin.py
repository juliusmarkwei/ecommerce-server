from django.contrib import admin
from . import models
from django.apps import apps


class CartModelAdmin(admin.ModelAdmin):
    list_display = ["created_by", "status", "created_at", "updated_at"]
    search_fields = ("status", "created_at", "updated_at")


class CartItemsModelAdmin(admin.ModelAdmin):
    list_display = ["cart_id", "product_id", "price", "quantity", "created_at"]
    search_fields = ("cart_id", "product_id", "price")


admin.site.register(models.Carts, CartModelAdmin)
admin.site.register(models.CartItems, CartItemsModelAdmin)
