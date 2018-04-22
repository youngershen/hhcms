# PROJECT : hhcms
# TIME : 18-4-15 下午6:50
# AUTHOR : Younger Shen
# CELL : 13811754531
# WECHAT : 13811754531
from hhcms.settings.production import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': env.db_url('DEFAULT_DATABASE_URL', default='mysql://root:root@127.0.0.1:3306/hhcms')
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@1o4_s8+lfapx2%c7azo6orns9p-o#9(b$96mkf#+3+kt1(gl_'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s : %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG'
        },
        'hhcms': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}
