from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
    """طلب العميل"""
    STATUS_CHOICES = [
        ('pending', 'قيد المعالجة'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="العميل")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"


class OrderItem(models.Model):
    """العناصر داخل الطلب"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
