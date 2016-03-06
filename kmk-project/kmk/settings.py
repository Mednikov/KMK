import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for kmk project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=n14+cx4vjcl9e-0w_rfl^*z#q_j6%*#**-tgg518nd*(a6va'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'kmk.urls'



WSGI_APPLICATION = 'kmk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'kmk', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'kmk', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',

    'kmk',
    'kmk.apps.staff',
    'kmk.apps.map',
    'kmk.apps.team',
    'kmk.apps.media',
    'kmk.apps.divider',
    'kmk.apps.grid',
)

LANGUAGES = (
    ## Customize this
    ('ru', gettext('ru')),
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'ru',
            'name': gettext('Русский'),
            'public': True,
            'redirect_on_fallback': True,
            'hide_untranslated': False,
        },
        {
            'code': 'en',
            'name': gettext('English'),
            'public': True,
            'redirect_on_fallback': True,
            'hide_untranslated': True,
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('fullwidth_narrow.html', 'Fullwidth Narrow'),
    ('sidebar_left.html', 'Sidebar Left'),
    # ('sidebar_left_submenu.html', 'Sidebar Left (Submenu)'),
    # ('sidebar_right.html', 'Sidebar Right'),
    ('services_list.html', 'Services List'),
    ('services_detail.html', 'Services Detail'),
    ('home.html', 'Home')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django'
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
