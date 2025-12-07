from django.contrib import admin
from .models import MenuItem, Order, OrderItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "price", "is_active")
    list_filter = ("is_active",)
    search_fields = ("code", "name")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("unit_price",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "created_at", "subtotal", "total")
    readonly_fields = ("subtotal", "service_charge", "discount_amount", "tax", "total", "created_at")
    inlines = [OrderItemInline]
