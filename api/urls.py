from . import views
from django.urls import path, re_path, include

app_name = "ecommerce_api"

urlpatterns = [
    path("users/<int:pk>/", views.UsersDetailView.as_view(), name="users-view"),
    path("users/", views.UsersListView.as_view(), name="users-list"),
    path("products/<int:pk>/", views.ProductsListView.as_view(), name="products-list"),
    path("products/", views.ProductsDetailView.as_view(), name="products-detail"),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("categories/", views.CategoryListViews.as_view(), name="category-list"),
    re_path("reviews/(?:(?P<pk>\d+)/)?$", views.ReviewView.as_view(), name="review"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order-detail"),
    path("orders/", views.OrdersListView.as_view(), name="order-list"),
    path("order-lines/", views.OrderLinesView.as_view(), name="order-lines"),
    path("carts/", views.CartsView.as_view(), name="carts-list"),
    path("cart-items/", views.CartItemsView.as_view(), name="cart-items"),
]
