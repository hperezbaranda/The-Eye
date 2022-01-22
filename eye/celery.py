import os
from celery import Celery
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
django.setup()

app = Celery('eye',
             backend='redis://localhost', 
             broker='redis://localhost:6379/0',
             include=['eye.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()