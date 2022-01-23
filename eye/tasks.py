from .models import Event
from celery import Celery

from eye.serializers import EventSerializer
from .celery import app


@app.task
def create_event(data):
    queryset = Event.objects.create(**data)
    queryset.save()
    
    return data

@app.task
def remove_event(id):
    query = Event.objects.get(pk = id)
    query.delete()