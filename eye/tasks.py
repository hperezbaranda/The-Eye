from .models import Event
from celery import Celery

from eye.serializers import EventSerializer
from .celery import app


@app.task
def create_event(data):
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
       
    return serializer.data

@app.task
def remove_event(id):
    query = Event.objects.get(pk = id)
    query.delete()