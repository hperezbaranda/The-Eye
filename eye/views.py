from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from debug.decorator import log_any_event
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response
from .tasks import create_event, remove_event
from django.db import transaction
from .log import getLog

logger = getLog("views.py")


class EventView(viewsets.ViewSet):
    """
    Class that implement come of CRUD operation for Event model
    """

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @log_any_event('Create Event','Creating event')
    def create(self, request):

        transaction.on_commit(lambda: create_event.delay(request.data))
        category = request.data["category"]
        name = request.data["name"]

        return Response(request.data, 201)

    @log_any_event('Destroy Event','Removing event')
    def destroy(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        transaction.on_commit(lambda: remove_event.delay(event.id))
        serializer = EventSerializer(event)
        return Response(serializer.data)