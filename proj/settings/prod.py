from .base import *

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}
ALLOWED_HOSTS = [
    'localhost',
    'wintercoding-todolist.herokuapp.com'
]

django_heroku.settings(locals())
