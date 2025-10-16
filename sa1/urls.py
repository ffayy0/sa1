from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 🔐 لوحة تحكم المدير
    path('admin/', admin.site.urls),

    # 🏬 روابط تطبيق المتجر (store)
    path('store/', include('store.urls')),

    # 🛒 روابط تطبيق الطلبات (orders)
    path('orders/', include('orders.urls')),

    # 👤 روابط تطبيق الحسابات (accounts)
    path('accounts/', include('accounts.urls')),
]
