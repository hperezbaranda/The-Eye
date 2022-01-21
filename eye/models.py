import uuid
from django.db import models


class DataEvent(models.Model):
    host = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    element = models.CharField(max_length=250, blank=True)

    def __str__(self) -> str:
        return self.host


class Event(models.Model):
    session = models.UUIDField(default=uuid.uuid4, editable=True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.ForeignKey(DataEvent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}-{self.category}"
