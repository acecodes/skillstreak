"""
Django settings for skillstreak project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

API_VERSION = r'1\.0'

LOGIN_URL = '/login/'
LOGOUT_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'streaks',
    'api',
    'oauth2_provider',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'rest_framework',
    'corsheaders',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
         'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 10,
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
     'read': 'Read scope',
     'write': 'Write scope',
     'groups': 'Access to your groups'
    }
}

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'skillstreak.urls'

WSGI_APPLICATION = 'skillstreak.wsgi.application'

AUTHENTICATION_BACKENDS = (
    "oauth2_provider.backends.OAuth2Backend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    )


TEMPLATE_CONTEXT_PROCESSORS = (
    # The next 3 are for django-allauth
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "django.contrib.auth.context_processors.auth",
    )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )

TABLE_PREFIX = {'system': 'sys_', 'core': 'core_', 'relation': 'rel_'}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)