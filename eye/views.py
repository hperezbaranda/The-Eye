from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from debug.decorator import log_any_event
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response
from .tasks import create_event, remove_event
from django.db import transaction
from .log import getLog
from rest_framework import status

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
        """
        Event detail view making the task in background and log every action using the decorator

        Args:
            
            pk (int, optional): Identifier for the event to be show. Defaults to None.

        Returns:
            Response: return the event showed
        """
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @log_any_event('Create Event')
    def create(self, request):
        """
        Event creation view making the task in background and log every action using the decorator

        Args:
            request (dict): Data to be store

        Returns:
            Response: return the event stored
        """
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

        # avoiding race condition
        transaction.on_commit(lambda: create_event.delay(request.data))

        return Response(request.data, status.HTTP_201_CREATED)
            

    @log_any_event('Destroy Event')
    def destroy(self, request, pk=None):
        """
        Event deletion view making the task in background and log every action using the decorator

        Args:
            
            pk (int, optional): Identifier for the event to be remove. Defaults to None.

        Returns:
            Response: return the event removed
        """
        event = get_object_or_404(Event, pk=pk)

        # avoiding race condition
        transaction.on_commit(lambda: remove_event.delay(event.id))

        serializer = EventSerializer(event)
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)