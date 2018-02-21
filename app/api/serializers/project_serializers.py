from api.models import Project
from rest_framework import serializers

class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['name','description','start_date', 'end_date', 'customer', 'users','active', 'created_at', 'updated_at']
