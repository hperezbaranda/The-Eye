import uuid
from django.db import models


class Event(models.Model):
    """
    Event model to be used as base for analysis
    """

    session_id = models.UUIDField(default=uuid.uuid4, editable=True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    data = models.JSONField(default=dict, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.category}"
