from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # ✅ لاستدعاء الصفحة الرئيسية home_view من داخل sa1/views.py

urlpatterns = [
    # 🔐 لوحة تحكم المدير
    path('admin/', admin.site.urls),

    # 🏠 الصفحة الرئيسية
    path('', views.home_view, name='home'),

    # 🏬 روابط تطبيق المتجر (store)
    path('store/', include('store.urls')),

    # 🛒 روابط تطبيق الطلبات (orders)
    path('orders/', include('orders.urls')),

    # 👤 روابط تطبيق الحسابات (accounts)
    path('accounts/', include('accounts.urls')),
]


# ✅ عرض الملفات الثابتة وملفات الوسائط أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
