"""
Django settings for MANTE project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# ===== Path base =====
BASE_DIR = Path(__file__).resolve().parent.parent

# ===== Cargar variables de entorno =====
load_dotenv(BASE_DIR / '.env')

# ===== Seguridad =====
SECRET_KEY = os.getenv('SECRET_KEY', 'inseguro-default')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# ALLOWED_HOSTS debe ser lista
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# ===== Aplicaciones =====
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps Me
    'apps.users',
    'apps.core',
    'apps.dashboard',
    'apps.mantenimiento',
    'apps.agenda',
    'apps.equipo',  
    
]

# ===== Middleware =====
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MANTE.urls'

# ===== Templates =====
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'MANTE.wsgi.application'

# ===== Base de Datos (SQL Server) =====
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'mssql'),
        'NAME': os.getenv('DB_NAME', 'pruebaSistemas'),
        'USER': os.getenv('DB_USER', 'sistemas'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'sistemas123'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '1433'),
        'OPTIONS': {
            'driver': os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server'),
            # Si usas autenticación Windows:
            # 'trusted_connection': 'yes',
        },
    }
}

# ===== Custom User =====
AUTH_USER_MODEL = 'users.CustomUser'


# ===== Password Validators =====
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ===== Internacionalización =====
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===== Static =====
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# ===== Auto Field =====
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
