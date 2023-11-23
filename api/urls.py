from . import views
from django.urls import path, include

app_name = "ecommerce_api"
urlpatterns = [
    path("users/", views.UsersList.as_view(), name="users"),
    # path("users/<int:pk>/", views.UsersRetrieve.as_view(), name="user-rud"),
    path('users/profiles/', views.SocialProfileList.as_view(), name="profiles"),
    path('users/profiles/<int:pk>/', views.SocialProfileRetrieve.as_view(), name="profiles-rud"),
    path("users/credentials/", views.CredentialsList.as_view(), name="credentials"),
    path("users/credentials/<int:pk>/", views.CredentialsRetrieve.as_view(), name="credentials-rud"),
    path("products/", views.ProductList.as_view(), name="products"),
    path("products/<int:pk>/", views.ProductRetrieve.as_view(), name="products-retrieve"),
    path("products/categories/", views.CategoriesList.as_view(), name="categories"),
    path("products/categories/<int:pk>/", views.CategoriesRetrieve.as_view(), name="categories-rud"),
    path("products/reviews/", views.ReviewList.as_view(), name="review"),
    path("products/reviews/<int:pk>", views.ReviewRetrieve.as_view(), name="review-rud"),
    path("orders/", views.OrderList.as_view(), name="orders"),
    path("orders/<int:pk>/", views.OrderRetrieve.as_view(), name="orders-rud"),
    path("order-lines/", views.OrderLinesList.as_view(), name="order-lines"),
    path("order-lines/<int:pk>/", views.OrderLinesRetrieve.as_view(), name="order-lines-rud"),
    path("carts/", views.CartsList.as_view(), name="carts-list"),
    path("carts/<int:pk>/", views.CartsRetieve.as_view(), name="carts-list-rud"),
    path("cart-items/", views.CartItemsList.as_view(), name="cart-items"),
    path("cart-items/<int:pk>/", views.CartItemsRetrieve.as_view(), name="cart-items-rud"),
]
