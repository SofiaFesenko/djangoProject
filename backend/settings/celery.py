import os

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
BROKER_TRANSPORT = 'redis'
CELERY_SEND_TASK_SENT_EVENT = True
