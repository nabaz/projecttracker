from rest_framework import generics
from api.models import Task
from api.serializers.task_serializers import TaskSerializers
from api.views.api_viewset import ApiViewSet

class TaskViewSet(ApiViewSet):
    model = Task
    serializer = TaskSerializers

    def get_queryset_for_user(self):
        return self.model.objects.filter(user = self.request.user)

    def get_serializer_class_for_user(self):
        return self.serializer
