from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from product.models import Products
import uuid


class Carts(models.Model):
    status_options = (
        ("active", "Active"),
        ("ordered", "Ordered"),
        ("pending", "Pending"),
        ("abandoned", "Abandoned"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(_("status"), max_length=20, choices=status_options)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.created_by.username

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItems(models.Model):
    cart_id = models.ForeignKey(
        Carts,
        verbose_name="cart_id",
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        Products,
        verbose_name="product_id",
        on_delete=models.CASCADE,
    )
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(_("created_at"), auto_now=True)

    def __str__(self):
        return self.cart_id + " - " + self.product_id

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
