from api.models import Customer
from rest_framework import serializers

class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['name','email','phone', 'address', 'web_url', 'note', 'active', 'created_at', 'updated_at']
