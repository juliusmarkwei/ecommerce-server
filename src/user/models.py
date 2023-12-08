from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_superuser(
        self, username, first_name, last_name, email, password, **other_fields
    ):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(
            username, first_name, last_name, email, password, **other_fields
        )

    def create_user(
        self, username, first_name, last_name, email, password, phone, **other_fields
    ):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    role_options = (("admin", "Admin"), ("staff", "Staff"), ("customer", "Customer"))
    locale_options = (
        ("en", "English"),
        ("fr", "French"),
        ("ru", "Russian"),
        ("ko", "Korean"),
        ("zh", "Chinese"),
        ("ha", "Hauza"),
    )

    slug = models.SlugField(
        verbose_name="A short label for URLs", max_length=100, blank=True, null=True
    )
    email = models.EmailField(_("email address"), max_length=100, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,12}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.",
    )
    phone = models.CharField(
        validators=[phone_regex], max_length=20, unique=True, blank=True, null=True
    )
    role = models.CharField(max_length=10, choices=role_options)
    username = models.CharField(_("user name"), max_length=100, unique=True)
    first_name = models.CharField(_("first name"), max_length=100, blank=True)
    last_name = models.CharField(_("last name"), max_length=100, blank=True)
    avatar = models.ImageField(
        _("profile picture"),
        upload_to="assets/customers/",
        max_length=100,
        blank=True,
    )
    locale = models.CharField(_("locale setting"), choices=locale_options)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    email_validated = models.BooleanField(default=False)
    phone_validated = models.BooleanField(default=False)
    bio = models.TextField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone", "first_name", "last_name"]

    def save(self, *args, **kwargs):
        if self.first_name and self.last_name:
            self.slug = slugify(self.first_name + self.last_name)
        else:
            self.slug = self.username
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-date_joined",)
