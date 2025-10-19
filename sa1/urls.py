from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔐 لوحة تحكم المدير
    path('admin/', admin.site.urls),

    # 🏬 روابط تطبيق المتجر (store)
    path('', include('store.urls')),  # ✅ اجعل تطبيق store مسؤول عن الصفحة الرئيسية

    # 🛒 روابط تطبيق الطلبات (orders)
    path('orders/', include('orders.urls')),

    # 👤 روابط تطبيق الحسابات (accounts)
    path('accounts/', include('accounts.urls')),
]


# ✅ عرض الملفات الثابتة (static) وملفات الوسائط (media) أثناء التطوير فقط
if settings.DEBUG:
    # ملفات الوسائط (مرفوعات المستخدمين مثل الصور)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # الملفات الثابتة (CSS, JS, صور الواجهة)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
