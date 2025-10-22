from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """تصنيف المنتج (مثل: إلكترونيات، ملابس، أثاث)"""
    name = models.CharField(max_length=100, unique=True, verbose_name="اسم التصنيف")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    """نموذج المنتج الأساسي"""
    name = models.CharField(max_length=150, verbose_name="اسم المنتج")
    description = models.TextField(blank=True, verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")

    # 🔗 ربط المنتج بتصنيف
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="التصنيف"
    )

    # ☁️ تخزين صورة المنتج في Cloudinary بدلاً من الملفات المحلية
    image = CloudinaryField("صورة المنتج", folder="products", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
