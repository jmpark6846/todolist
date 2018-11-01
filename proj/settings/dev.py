from .base import *

DEBUG = True


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

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
