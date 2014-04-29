# -*- coding: utf-8 -*-
"""
Django settings for ada project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
try:
    from S3 import CallingFormat
    AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
except ImportError:
    # TODO: Fix this where even if in Dev this class is called.
    pass

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
TIME_ZONE = 'America/Phoenix' # Time zone warning

########## 3RD PARTY FORKS
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
GRAPPELLI_INSTALLED = True
TESTING = False
ALLOWED_HOSTS = ["*"]
FILE_UPLOAD_PERMISSIONS = 0o644
########## END 3RD PARTY FORKS

class Common(Configuration):

    ########## APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",
        'django.contrib.messages',
        'django.contrib.comments',
        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'south',  # Database migration helpers:
        'crispy_forms',  # Form layouts
        'avatar',  # for user avatars
        "mezzanine.boot",
        "mezzanine.conf",
        "mezzanine.core",
        "mezzanine.generic",
        "mezzanine.blog",
        "mezzanine.forms",
        "mezzanine.pages",
        "mezzanine.galleries",
        "mezzanine.twitter",
        #"mezzanine.accounts",
        #"mezzanine.mobile",
    )

    OPTIONAL_APPS = (
        #"compressor",
        "django_extensions",
        PACKAGE_NAME_FILEBROWSER,
        PACKAGE_NAME_GRAPPELLI,
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        #'users',  # custom users app
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS =  OPTIONAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    INSTALLED_APPS += (
        # Needs to come last for now because of a weird edge case between
        #   South and allauth
        'allauth',  # registration
        'allauth.account',  # registration
        'allauth.socialaccount',  # registration
    )
    ########## END APP CONFIGURATION

    ########## MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        'mezzanine.core.middleware.UpdateCacheMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        "django.contrib.messages.middleware.MessageMiddleware",
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        #^might reomve
        "mezzanine.core.request.CurrentRequestMiddleware",
        "mezzanine.core.middleware.RedirectFallbackMiddleware",
        "mezzanine.core.middleware.TemplateForDeviceMiddleware",
        "mezzanine.core.middleware.TemplateForHostMiddleware",
        "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
        "mezzanine.core.middleware.SitePermissionMiddleware",
        # Uncomment the following if using any of the SSL settings:
        # "mezzanine.core.middleware.SSLRedirectMiddleware",
        "mezzanine.pages.middleware.PageMiddleware",
        "mezzanine.core.middleware.FetchFromCacheMiddleware",
    )
    ########## END MIDDLEWARE CONFIGURATION

    ########## DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(True)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    ########## END DEBUG

    ########## SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    #       In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = "CHANGEME!!!"
    NEVERCACHE_KEY = "f60ab341-980b-43f5-94e6-134f610bce50b117c5b5-4a00-420e-b1d3-41b5a88ee3320ecf6530-5682-4e73-a70e-06926bcb4013"
    ########## END SECRET CONFIGURATION

    ########## FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )
    ########## END FIXTURE CONFIGURATION

    ########## MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('goldhand', 'will@django.nu'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    ########## END MANAGER CONFIGURATION

    ########## DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue('postgres://localhost')
    ########## END DATABASE CONFIGURATION

    ########## CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc memcacheify is painful to install on windows.
    # memcacheify is what's used in Production
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
        }
    }

    CACHE_MIDDLEWARE_KEY_PREFIX = 'ada'


    ########## END CACHING

    ########## GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'America/Phoenix'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    ########## END GENERAL CONFIGURATION

    ########## TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
        "mezzanine.conf.context_processors.settings",
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )

    # See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
    CRISPY_TEMPLATE_PACK = 'bootstrap3'
    ########## END TEMPLATE CONFIGURATION

    ########## MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION

    ########## URL Configuration
    ROOT_URLCONF = 'config.urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'config.wsgi.application'
    ########## End URL Configuration

    ########## AUTHENTICATION CONFIGURATION
    #AUTHENTICATION_BACKENDS = (
    #    "django.contrib.auth.backends.ModelBackend",
    #    "allauth.account.auth_backends.AuthenticationBackend",
    #)
    AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

    # Some really nice defaults
    ACCOUNT_AUTHENTICATION_METHOD = "username"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"

    ########## END AUTHENTICATION CONFIGURATION

    ########## AUTHENTICATION PROVIDERS

    #INSTALLED_APPS += (
        #'allauth.socialaccount.providers.bitly',
        #'allauth.socialaccount.providers.dropbox',
        #'allauth.socialaccount.providers.facebook',
        #'allauth.socialaccount.providers.github',
        #'allauth.socialaccount.providers.google',
        #'allauth.socialaccount.providers.linkedin',
        #'allauth.socialaccount.providers.openid',
        #'allauth.socialaccount.providers.persona',
        #'allauth.socialaccount.providers.soundcloud',
        #'allauth.socialaccount.providers.stackexchange',
        #'allauth.socialaccount.providers.twitch',
        #'allauth.socialaccount.providers.twitter',
        #'allauth.socialaccount.providers.vimeo',
        #'allauth.socialaccount.providers.vk',
        #'allauth.socialaccount.providers.weibo',
    #)

    #SOCIALACCOUNT_PROVIDERS = \
    #    { 'facebook':
    #          { 'SCOPE': ['email', 'publish_stream'],
    #            'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
    #            'METHOD': 'o'}
    #    }

    ########## END AUTHENTICATION PROVIDERS



    ########## Custom user app defaults
    # Select the correct user model
    #AUTH_USER_MODEL = "users.User"
    #LOGIN_REDIRECT_URL = "users:redirect"
    ########## END Custom user app defaults

    ########## SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    ########## END SLUGLIFIER

    ########## LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    ########## END LOGGING CONFIGURATION


    ########## Your common stuff: Below this line define 3rd party libary settings
    TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)



class Local(Common):

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS

    ########## Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    ########## End mail settings

    ########## django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    ########## end django-debug-toolbar

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = 'staticfiles'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    FILE_UPLOAD_PERMISSIONS = 0644

    ########## END STATIC FILE CONFIGURATION

    ########## django-extensions
    INSTALLED_APPS += ('django_extensions',)
    ########## end django-extensions

    ########## DATABASE CONFIGURATION
    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ada-goldhand',
            'USER': 'goldhand',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
    }
    ########## END DATABASE CONFIGURATION

    ########## Your local stuff: Below this line define 3rd party libary settings


class Production(Common):

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS

    ########## SECRET KEY
    SECRET_KEY = values.SecretValue()
    NEVERCACHE_KEY = "f60ab341-980b-43f5-94e6-134f610bce50b117c5b5-4a00-420e-b1d3-41b5a88ee3320ecf6530-5682-4e73-a70e-06926bcb4013"
    ########## END SECRET KEY

    ########## django-secure
    #INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
    #SECURE_HSTS_SECONDS = 60
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    #SECURE_FRAME_DENY = True
    #SECURE_CONTENT_TYPE_NOSNIFF = True
    #SECURE_BROWSER_XSS_FILTER = True
    #SESSION_COOKIE_SECURE = True
    #SESSION_COOKIE_HTTPONLY = True
    #SECURE_SSL_REDIRECT = True
    ########## end django-secure

    ########## SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    ########## END SITE CONFIGURATION

    INSTALLED_APPS += ("gunicorn", )

    ########## STORAGE CONFIGURATION
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += (
        'storages',
    )

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
    AWS_ACCESS_KEY_ID = values.SecretValue()
    AWS_SECRET_ACCESS_KEY = values.SecretValue()
    AWS_STORAGE_BUCKET_NAME = values.SecretValue()
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIREY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY,
            AWS_EXPIREY)
    }

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    #STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = 'https://s3.amazonaws.com/%s/' % "djangonu-ada"
    MEDIA_URL = 'https://s3.amazonaws.com/%s/' % "djangonu-ada"
    ########## END STORAGE CONFIGURATION

    ########## EMAIL
    DEFAULT_FROM_EMAIL = values.Value(
            'ada <ada-noreply@ada.herokuapp.com>')
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    EMAIL_HOST = values.Value('smtp.sendgrid.com')
    EMAIL_HOST_PASSWORD = values.SecretValue(environ_prefix="", environ_name="SENDGRID_PASSWORD")
    EMAIL_HOST_USER = values.SecretValue(environ_prefix="", environ_name="SENDGRID_USERNAME")
    EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
    EMAIL_SUBJECT_PREFIX = values.Value('[ada] ', environ_name="EMAIL_SUBJECT_PREFIX")
    EMAIL_USE_TLS = True
    SERVER_EMAIL = EMAIL_HOST_USER
    ########## END EMAIL

    ########## TEMPLATE CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
    ########## END TEMPLATE CONFIGURATION

    ########## CACHING
    # Only do this here because thanks to django-pylibmc-sasl and pylibmc memcacheify is painful to install on windows.
    #CACHES = values.CacheURLValue(default="memcached://mc4.dev.ec2.memcachier.com:11211")
    os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
    os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

    CACHES = {
      'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': { 'tcp_nodelay': True }
      }
    }
    ########## END CACHING



    ########## Your production stuff: Below this line define 3rd party libary settings