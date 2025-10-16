from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """لعرض عناصر الطلب داخل صفحة الطلب"""
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    ordering = ('-created_at',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    search_fields = ('product__name',)
