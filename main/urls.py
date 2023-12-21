from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework.permissions import AllowAny


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version="v1",
        description="A fully functional Ecommerce - Django Rest API project build and tested with restframework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="Developer", email="juliusmarkwei2000@gmail.com",),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
    
)

urlpatterns = [    
    #default drf authentincation
    path("api-auth/", include("rest_framework.urls")),
    
    #drf jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-redoc")
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
