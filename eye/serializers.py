
from datetime import datetime
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer to handle the data model

    Raises:
        serializers.ValidationError: Data validation before save into database
    """
    class Meta:
        model = Event
        fields = ('session_id', 'category', 'name', 'timestamp', 'data')

    def validate_timestamp(self, value):
        """
        Method to validate timestamp field
          - Must be in a correct format
          - Could not be a future data
        Args:
            value (datetime): Timestamp value to be validated

        Raises:
            serializers.ValidationError: Raise a validation error (format or future value)
        """
        format = "%Y-%m-%d %I:%M:%S.%f%z"
        datetime.strptime(str(value),format)

        if value > datetime.now(value.tzinfo):
            raise serializers.ValidationError("Can not be event in the future")