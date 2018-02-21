from api.models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name', 'description', 'project', 'user', 'active', 'created_at', 'updated_at']
