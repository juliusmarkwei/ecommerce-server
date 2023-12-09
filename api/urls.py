from . import views
from django.urls import path, re_path, include

app_name = "ecommerce_api"

urlpatterns = [
    path("users/", views.UsersView.as_view(), name="users-view"),
    re_path("products/(?:(?P<pk>\d+)/)?$", views.ProductsView.as_view(), name="products"),
    re_path("products/categories/(?:(?P<pk>\d+)/)?$", views.CategoriesViews.as_view(), name="categories"),
    re_path("products/reviews/(?:(?P<pk>\d+)/)?$", views.ReviewView.as_view(), name="review"),
    re_path("orders/(?:(?P<pk>\d+)/)?$", views.OrdersView.as_view(), name="orders"),
    path("order-lines/", views.OrderLinesView.as_view(), name="order-lines"),
    path("carts/", views.CartsView.as_view(), name="carts-list"),
    path("cart-items/", views.CartItemsView.as_view(), name="cart-items"),
    # path("verify-email", views.VerifyEmail.as_view(), name="verify-email")
]
