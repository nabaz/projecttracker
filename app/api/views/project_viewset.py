from rest_framework import generics
from api.models import Project
from api.serializers.project_serializers import ProjectSerializers
from api.views.api_viewset import ApiViewSet

class ProjectViewSet(ApiViewSet):

    model = Project
    serializer = ProjectSerializers

    def get_queryset_for_user(self):
        return self.model.objects.filter(users = self.request.user)
