from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """ملف المستخدم الإضافي"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="المدينة")

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return f"الملف الشخصي لـ {self.user.username}"
