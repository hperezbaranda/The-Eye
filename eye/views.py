from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event
from rest_framework.decorators import action


class EventView(viewsets.ModelViewSet):
    """
    Class that implement the CRUD operation for Event model
    """

    serializer_class = EventSerializer
    queryset = Event.objects.all()
