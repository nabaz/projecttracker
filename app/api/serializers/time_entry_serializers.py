from api.models import TimeEntry
from rest_framework import serializers


class TimeEntrySerializers(serializers.ModelSerializer):

    class Meta:
        model = TimeEntry
        fields = '__all__'
