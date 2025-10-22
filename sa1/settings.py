from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from decouple import config

# 📂 المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 إعدادات الأمان من ملف .env
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

# 🌐 المضيفون المسموح بهم (تُقرأ من ملف .env)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')

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
    'store',
    'orders',
    'accounts',
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

# 🗃️ قاعدة البيانات (SQLite في التطوير، PostgreSQL في الإنتاج)
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE'),
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
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

# 🖼️ إعداد الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ☁️ إعداد Cloudinary لتخزين الميديا
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY': config('API_KEY'),
    'API_SECRET': config('API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ☁️ تهيئة الاتصال بـ Cloudinary (يعمل في كل السياقات)
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)

# 📸 إعداد روابط الوسائط (تدار من Cloudinary)
MEDIA_URL = '/media/'

# 🧱 الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🧩 رسائل تصحيحية في وضع التطوير
print(f"📁 [DEBUG] Templates Directory: {os.path.join(BASE_DIR, 'templates')}")
print("☁️ [DEBUG] Cloudinary linked successfully to your project ✅")
if DEBUG:
    print("💾 [DEBUG] Using SQLite (Development)")
else:
    print("🗄️ [PRODUCTION] Connected to PostgreSQL Database successfully ✅")
  