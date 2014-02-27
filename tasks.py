from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')
#app = Celery('tasks', broker='amqp://guest@localhost//')
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
)

@app.task
def add(x, y):
    return x + y
