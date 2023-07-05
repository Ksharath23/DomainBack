from rest_framework import serializers
from .models import Employee, Domain, Subdomain

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('__all__')

class SubdomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdomain
        fields = ('__all__')