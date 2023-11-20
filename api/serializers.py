from rest_framework.serializers import ModelSerializer
from user import models


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            "id",
            "email",
            "phone",
            "role",
            "username",
            "first_name",
            "last_name",
            "avatar",
            "locale",
            "bio",
            "company",
        ]


class SocialProfileSerializer(ModelSerializer):
    class Meta:
        model = models.SocialProfile
        fields = ["id", "user_id", "platform", "platform_user"]


class CredentialsSerializer(ModelSerializer):
    class Meta:
        model = models.Credentials
        fields = [
            "id",
            "provider_id",
            "provider_key",
            "user",
            "hasher",
            "password_hash",
            "password_salt",
        ]
