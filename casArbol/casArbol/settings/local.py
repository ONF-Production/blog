import os
from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_casArbol',
        'USER': 'root',
        'PASSWORD': 'sandra4321',
        'HOST': 'localhost',
        'PORT': '3306',
=======
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlit3'),
>>>>>>> c1d29e8f6733f63ed287830f96a6df64fe75e8fe
    }
}

