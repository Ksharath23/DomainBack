from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
import datetime
from rest_framework.decorators import APIView

from .models import *

from .serializers import *

class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        try:
            employee = Employee.objects.get(id=request.data['id'])
        except Employee.DoesNotExist:
            return Response({'error': 'Post does not exist.'})
        
        serializer = Employee(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DomainProviderView(APIView):
    def get(self, request):
        domains = DomainProvider.objects.all()
        serializer = DomainProviderSerializer(domains, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DomainProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        try:
            domain = DomainProvider.objects.get(id=request.data['id'])
            print("result:",domain)
        except DomainProvider.DoesNotExist:
            return Response({'error': 'Post does not exist.'})
        
        serializer = DomainProviderSerializer(domain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class DomainView(APIView):
    def get(self, request):
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        try:
            domain = Domain.objects.get(id=request.data['id'])
        except Domain.DoesNotExist:
            return Response({'error': 'Post does not exist.'})
        
        serializer = DomainSerializer(domain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AllDomains(generics.ListAPIView):
    serializer_class = DomainSerializer

    def list(self, request):
        query_set = Domain.objects.filter(parent_domain__isnull = True)
        serializer = self.get_serializer(query_set,many=True)
        return Response({"result:":serializer.data})
    
class AllSubdomains(generics.ListAPIView):
    serializer_class = DomainSerializer

    def list(self, request):
        query_set = Domain.objects.filter(parent_domain__isnull = False)
        serializer = self.get_serializer(query_set,many=True)
        return Response({"result:":serializer.data}) 

class SubdomainsbyDomains(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        domain_name = self.request.query_params.get('domain_name')
        query_set = Domain.objects.filter(parent_domain__name__icontains = domain_name)
        serializer = self.get_serializer(query_set,many=True)
        return Response({"result:":serializer.data}) 

class DomainsSearch(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        Filter_Name = self.request.query_params.get('Filter_Name')
        Filter_Value = self.request.query_params.get('Filter_Value')
        query_dict = {}
        temp = str(Filter_Name)+'__icontains'
        query_dict['parent_domain__isnull'] = True
        query_dict[temp] = Filter_Value
        query = Domain.objects.filter(**query_dict)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})

class DomainsFilter(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        name = self.request.query_params.get('name')
        registrar = self.request.query_params.get('registrar')
        created_at = self.request.query_params.get('created_at')
        expiry_date = self.request.query_params.get('expiry_date')
        query_dict = {}
        query_dict['parent_domain__isnull'] = True
        if name:
            query_dict['name__icontains'] = name
        if registrar:
            query_dict['registrar__id'] = registrar
        if created_at:
            date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
            query_dict['created_at__gt'] = date
        if expiry_date:
            date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")
            query_dict['expiry_date__lt'] = date

        query = Domain.objects.filter(**query_dict)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})

class SubDomainsSearch(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        Filter_Name = self.request.query_params.get('Filter_Name')
        Filter_Value = self.request.query_params.get('Filter_Value')
        query_dict = {}
        temp = str(Filter_Name)+'__icontains'
        query_dict['parent_domain__isnull'] = False
        query_dict[temp] = Filter_Value
        query = Domain.objects.filter(**query_dict)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})

class SubDomainsFilter(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        
        name = self.request.query_params.get('name')
        registrar = self.request.query_params.get('Registrar')
        created_at = self.request.query_params.get('created_at')
        expiry_date = self.request.query_params.get('expiry_date')
        query_dict = {}
        query_dict['parent_domain__isnull'] = False
        if name:
            query_dict['name__icontains'] = name
        if registrar:
            query_dict['registrar__id'] = registrar
        if created_at:
            date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
            query_dict['created_at__gt'] = date
        if expiry_date:
            date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")
            query_dict['expiry_date__lt'] = date

        query = Domain.objects.filter(**query_dict)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})



