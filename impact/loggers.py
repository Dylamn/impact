from django.utils.log import RequireDebugTrue
LOGGERS = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'debug': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'verbose': {
            'style': '{',
            'format':
                '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
        },
        'simple': {
            'style': '{',
            'format': '{levelname} {message}',
        }
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/impact/django/warning.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
