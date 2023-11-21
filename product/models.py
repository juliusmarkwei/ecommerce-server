from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Categories(models.Model):
    parent_category = models.ForeignKey(
        "self",  # References the same model
        on_delete=models.SET_NULL,  # What to do when the parent category is deleted
        null=True,  # Allows for top-level categories with no parent
        blank=True,  # It's not required to have a parent category
        related_name="subcategories",  # How to access the children of a category
    )
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically set the slug based on the name
        if not self.slug:
            self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Products(models.Model):
    discount_type_options = (
        ("none", "None"),
        ("percent", "Percent"),
        ("amount", "Amount"),
        ("currency", "Currency"),
    )
    category = models.ForeignKey(
        Categories,
        verbose_name="category_id",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("product title"), max_length=200)
    picture = models.ImageField(_("image of product"), upload_to="assets/products/")
    summary = models.TextField(_("product summary"), max_length=200)
    description = models.TextField(_("product description"), max_length=200)
    price = models.FloatField(_("product price (GH)"), default=0.0)
    discount_type = models.CharField(
        _("discount type"), max_length=10, choices=discount_type_options
    )
    discount_value = models.FloatField(_("discount value"), default=0.0)
    tags = models.CharField(_("tags"), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Reviews(models.Model):
    rating_options = (
        ("poor", "Poor"),
        ("unsatisfactory", "Unsatisfactory"),
        ("satisfactory", "Satisfactory"),
        ("very satisfactory", "Very Satisfactory"),
        ("outstanding", "Outstanding"),
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user_id",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Products,
        verbose_name="product_id",
        on_delete=models.CASCADE,
    )
    rating = models.CharField(max_length=30, choices=rating_options)
    comments = models.TextField(_("comments"), max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id + " - " + self.product

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
