from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist',
        'USER': 'admin',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
