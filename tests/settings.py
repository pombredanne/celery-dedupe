BROKER_URL = 'redis://localhost:6379/9'
CELERY_ALWAYS_EAGER = False
CELERY_IMPORTS = ('tests.test_task',)
CELERY_RESULT_BACKEND = 'redis://localhost:6379/9'
