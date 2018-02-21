from rest_framework import generics
from rest_framework import viewsets
from api.models import Customer
from api.serializers.customer_serializers import CustomerSerializers
from api.views.api_viewset import ApiViewSet, RoleError

class CustomerViewSet(ApiViewSet):
    serializer = CustomerSerializers
    model = Customer

    def get_queryset_for_user(self):
        raise RoleError("you don't have access to customer")
