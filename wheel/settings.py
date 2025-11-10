"""
Django settings for wheel project — production-ready for Render deployment.
"""

from pathlib import Path
import os
import dj_database_url  # ✅ Helps load DB info from Render’s environment

BASE_DIR = Path(__file__).resolve().parent.parent


# ⚠️ SECURITY WARNING: keep secret keys out of code!
# Render will provide this via Environment Variables (you’ll set it in dashboard)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key-for-dev")

# ✅ Turn OFF debug in production
DEBUG = os.environ.get("DEBUG", "False") == "True"

# ✅ Allow Render’s domain or your local host
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']


# -----------------------------
#  Installed apps and middleware
# -----------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'info',
    'blog',
    'shop',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ serve static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wheel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.categories_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'wheel.wsgi.application'


# -----------------------------
#  Database Configuration
# -----------------------------

# ✅ Use Render’s DATABASE_URL if present, else fallback to your local Postgres
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:Guler@localhost:5432/wheel_project',
        conn_max_age=600
    )
}


# -----------------------------
#  Password validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------
#  Internationalization
# -----------------------------
LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('az', 'Azerbaijani'),
    ('en', 'English'),
    ('ru', 'Russian'),
]

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [BASE_DIR / 'locale']


# -----------------------------
#  Static & Media Files
# -----------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ✅ Where all static files will be collected for Render
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ Optional: let Whitenoise compress and cache files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR / 'media'


# -----------------------------
#  Default primary key field
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
