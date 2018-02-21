from rest_framework import generics
from api.models import TimeEntry
from api.serializers.time_entry_serializers import TimeEntrySerializers
from api.views.api_viewset import ApiViewSet

class TimeEntryViewSet(ApiViewSet):
    model = TimeEntry
    serializer = TimeEntrySerializers

    def get_queryset_for_user(self):
        return self.model.objects.filter(user = self.request.user)
