from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان - لا تستخدم هذا المفتاح في الإنتاج
SECRET_KEY = 'django-insecure-%xm*i-*fw0-&bolaosrzp717wydltjxwgots%eu7ck7b#o^qi5'

# تفعيل وضع التطوير
DEBUG = True

# السماح بالمضيفين (أضف لاحقاً نطاق موقعك عند الإطلاق)
ALLOWED_HOSTS = []


# التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🏬 تطبيقات المشروع الخاصة بالمتجر الإلكتروني
    'store',     # إدارة المنتجات والتصنيفات والمخزون
    'orders',    # إدارة السلة والطلبات والفواتير
    'accounts',  # إدارة المستخدمين والتوثيق
]


# الوسائط الوسطى (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # دعم اللغة والتوقيت
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ملف روابط المشروع
ROOT_URLCONF = 'sa1.urls'


# إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # يمكنك إضافة مسار القوالب العامة هنا لاحقاً مثل:
        # 'DIRS': [BASE_DIR / 'templates'],
        'DIRS': [],
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


# تطبيق WSGI
WSGI_APPLICATION = 'sa1.wsgi.application'


# قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'              # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'         # التوقيت المحلي للرياض
USE_I18N = True                   # تفعيل الترجمة
USE_L10N = True                   # تنسيق التواريخ والأرقام
USE_TZ = True                     # استخدام المنطقة الزمنية


# الملفات الثابتة (Static Files)
STATIC_URL = 'static/'
# يمكنك لاحقاً إضافة:
# STATICFILES_DIRS = [BASE_DIR / 'static']

# الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
