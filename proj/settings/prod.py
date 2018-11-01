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

django_heroku.settings(locals())
