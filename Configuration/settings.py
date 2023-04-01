import logging
import logging.config
import mysql.connector
import configparser
from django.conf import settings

# Load the configuration for the server, database, and logging
config = configparser.ConfigParser()
config.read('server.conf')

# Server configuration options
server_host = config['server']['host']
server_port = config['server']['port']
server_debug = config.getboolean('server', 'debug')

# Database configuration options
db_host = config['database']['host']
db_port = config['database']['port']
db_user = config['database']['user']
db_password = config['database']['password']
db_database = config['database']['database']

# Logging configuration options
log_file = config['logging']['log_file']
log_level = config['logging']['log_level']

# Django settings
DEBUG = server_debug

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_database,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': log_file,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': log_level,
        },
    },
}

# Connect to the database
conn = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database
)

# Configure the logging
logging.basicConfig(filename=log_file, level=log_level)
