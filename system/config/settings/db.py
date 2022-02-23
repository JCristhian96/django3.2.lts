from operator import imod
from .base import os, BASE_DIR

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child(os.getenv("DB_LOCAL")),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_PROD_NAME'),
        'USER': os.getenv('DB_PROD_USER'),
        'PASSWORD': os.getenv('DB_PROD_PASS'),
        'HOST': 'localhost',
        'PORT': 5432
    }
}