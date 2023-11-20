from . import views
from django.urls import path, include

app_name = "user"
urlpatterns = [
    path("", views.UserView.as_view(), name="user-list"),
    path("<int:pk>/", views.RetrieveUser.as_view(), name="user-retieve"),
    path('social-profiles/', views.SocialProfileList.as_view(), name="social-profiles"),
    path('social-profiles/<int:pk>/', views.SocialProfileRetrieve.as_view(), name="social-profiles-retrieve"),
    path("credentials/", views.CredentialsList.as_view(), name="user-credentials"),
    path("credentials/<int:pk>/", views.CredentialsRetrieve.as_view(), name="user-credentials-retrieve"),
]


