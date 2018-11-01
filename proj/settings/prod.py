from .base import *

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist',
        'USER': 'joonmo',
        'PASSWORD': 'todolist1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
ALLOWED_HOSTS = [
    'localhost',
    'wintercoding-todolist.herokuapp.com'
]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
django_heroku.settings(locals())
