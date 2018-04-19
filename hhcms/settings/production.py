# PROJECT : hhcms
# TIME : 18-4-15 下午6:50
# AUTHOR : Younger Shen
# CELL : 13811754531
# WECHAT : 13811754531

from hhcms.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': env.db_url('DEFAULT_DATABASE_URL')
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

WSGI_APPLICATION = 'hhcms.wsgi.application'

ROOT_URLCONF = 'hhcms.urls.patterns'

INSTALLED_APPS += [
    'hhcms.apps.common',
    'hhcms.apps.account',
    'hhcms.apps.content',
    'hhcms.apps.seo',
    'hhcms.apps.wechat'
]
