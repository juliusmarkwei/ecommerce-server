from django.contrib import admin
from django.apps import apps
from src.order.models import OrderLines, Orders


class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at"]
    search_fields = ["user"]
    

class OrderLinesModelAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product", "price", "quantity"]
    
admin.site.register(Orders, OrdersModelAdmin)
admin.site.register(OrderLines, OrderLinesModelAdmin)