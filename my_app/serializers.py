from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('__all__')

class DomainProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainProvider
        fields = ('__all__')