from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_casArbol',
        'USER': 'root',
        'PASSWORD': 'sandra4321',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

