from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
    openapi.Info(
        title="ECOMMERCE API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="juliusmarkwei2000@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #Oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    
    #default drf suthentincation
    path("api-auth/", include("rest_framework.urls")),
    
    #drf jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("",schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui",),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
