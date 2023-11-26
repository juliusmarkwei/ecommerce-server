from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from src.product.models import Products


class Carts(models.Model):
    status_options = (
        ("active", "Active"),
        ("ordered", "Ordered"),
        ("pending", "Pending"),
        ("abandoned", "Abandoned"),
    )
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(_("status"), max_length=20, choices=status_options)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.created_by.username

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        unique_together = (
            "id",
            "created_by",
        )


class CartItems(models.Model):
    id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(
        Carts,
        verbose_name="cart",
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        Products,
        verbose_name="product",
        on_delete=models.CASCADE,
    )
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(_("created_at"), auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.product_id)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
