import uuid
from django.db import models
from django.forms import JSONField


class DataEvent(models.Model):
    """
    Data payload for every event
    """
    
    host = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    rest_data = models.JSONField(db_index=True, blank=True)

    def __str__(self) -> str:
        return self.host


class Event(models.Model):
    """
    Event model to be used as base for analysis
    """
    session = models.UUIDField(default=uuid.uuid4, editable=True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.ForeignKey(DataEvent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}-{self.category}"
