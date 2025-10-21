from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# 📂 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ مفتاح الأمان (لا تستخدم هذا المفتاح في بيئة الإنتاج)
SECRET_KEY = 'django-insecure-%xm*i-*fw0-&bolaosrzp717wydltjxwgots%eu7ck7b#o^qi5'

# 🔧 وضع التطوير
DEBUG = True

# 🌐 المضيفون المسموح بهم
ALLOWED_HOSTS = []


# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    # 🧱 تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ☁️ تطبيقات Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # 🏬 تطبيقات المشروع الخاصة
    'store',     # إدارة المنتجات والصفحة الرئيسية
    'orders',    # إدارة الطلبات والفواتير
    'accounts',  # إدارة المستخدمين والتوثيق
]


# ⚙️ الوسائط الوسطى (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 🌍 دعم اللغة والتوقيت
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🔗 ملف روابط المشروع
ROOT_URLCONF = 'sa1.urls'


# 🧱 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 🚀 تطبيق WSGI
WSGI_APPLICATION = 'sa1.wsgi.application'


# 🗃️ قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌍 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# 🖼️ إعداد الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ☁️ إعداد Cloudinary لتخزين ملفات الميديا
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dptrz53hn',
    'API_KEY': '877719151785919',
    'API_SECRET': 'D0saL3JKkJORvkW5eInC9ZSQNPI',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# 📸 إعداد روابط الوسائط (سيتم توليدها من Cloudinary مباشرة)
MEDIA_URL = '/media/'


# 🧱 الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 🧩 طباعة المسار أثناء التطوير (اختياري لتأكيد المسار الصحيح)
print(f"📁 [DEBUG] Templates Directory: {os.path.join(BASE_DIR, 'templates')}")
print("☁️ [DEBUG] Cloudinary linked successfully to your project ✅")
