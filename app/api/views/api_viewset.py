from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from api.models import Project

from drf_roles.mixins import RoleViewSetMixin

class RoleError(Exception):
    """Base class for exceptions in this module."""
    pass

class ApiViewSet(RoleViewSetMixin, viewsets.ModelViewSet, Exception):
    permission_classes = (IsAuthenticated,)

    def get_queryset_for_admin(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        return self.serializer

    def perform_create(self, serializer):
        serializer.save(creator_id = self.request.user.id)
