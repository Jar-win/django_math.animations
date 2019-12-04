"""
Django settings for FOSSEE_math project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ses_=j4dd31z!k-tnszg+gravu0v-vtn4*#6i8z5n2buje1rk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'phonenumber_field',
    'fossee_math_pages.apps.FosseeMathPagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'froala_editor',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FOSSEE_math.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'FOSSEE_math.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'FOSSEE_math/static')
]

FROALA_UPLOAD_PATH = "fossee_math/uploads/froala_editor/"

FROALA_IMAGE_UPLOAD_PATH = 'fossee_math/uploads/froala_editor/images/'

FROALA_FILE_UPLOAD_PATH = 'fossee_math/uploads/froala_editor/files/'


LOGIN_URL = '/login/'

MEDIA_URL = '/data/'

MEDIA_ROOT = os.path.join(BASE_DIR, "fossee_math", 'data')

LOG_FOLDER = os.path.join(BASE_DIR, "fossee_math", "logs")

LOGOUT_REDIRECT_URL = "/"

FRAOLA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')
FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'draggable', 'emoticons',
                         'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image',
                         'inline_style',
                         'line_breaker', 'link', 'html', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert',
                         'quote', 'save', 'table',
                         'url', 'video')
FROALA_INCLUDE_JQUERY = True


# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER='shiju.ka@mca.christuniversity.in'
EMAIL_HOST_PASSWORD='39676880'
EMAIL_USE_TLS = True