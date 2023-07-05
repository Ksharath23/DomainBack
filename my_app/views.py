from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from .models import Employee, Domain, Subdomain
from .serializers import EmployeeSerializer, DomainSerializer, SubdomainSerializer
import datetime
from rest_framework.decorators import APIView

# class EmployeeCreate(generics.CreateAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class EmployeeList(generics.ListAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class EmployeeUpdate(generics.RetrieveUpdateAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class EmployeeDelete(generics.RetrieveDestroyAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

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
        
        serializer = Domain(domain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class SubdomainView(APIView):
    def get(self, request):
        subdomains = Subdomain.objects.all()
        serializer = SubdomainSerializer(subdomains, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SubdomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request):
        try:
            subdomain = Subdomain.objects.get(id=request.data['id'])
        except Subdomain.DoesNotExist:
            return Response({'error': 'Post does not exist.'})
        
        serializer = Employee(subdomain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# class DomainCreate(generics.CreateAPIView):
#     serializer_class = DomainSerializer
#     queryset = Domain.objects.all()

# class DomainList(generics.ListAPIView):
#     serializer_class = DomainSerializer
#     queryset = Domain.objects.all()

# class DomainUpdate(generics.RetrieveUpdateAPIView):
#     serializer_class = DomainSerializer
#     queryset = Domain.objects.all()

# class DomainDelete(generics.RetrieveDestroyAPIView):
#     serializer_class = DomainSerializer
#     queryset = Domain.objects.all()


# class SubDomainCreate(generics.CreateAPIView):
#     serializer_class = SubdomainSerializer
#     queryset = Subdomain.objects.all()

# class SubDomainList(generics.ListAPIView):
#     serializer_class = SubdomainSerializer
#     queryset = Subdomain.objects.all()

# class SubDomainUpdate(generics.RetrieveUpdateAPIView):
#     serializer_class = SubdomainSerializer
#     queryset = Subdomain.objects.all()

# class SubDomainDelete(generics.RetrieveDestroyAPIView):
#     serializer_class = SubdomainSerializer
#     queryset = Subdomain.objects.all()
class TestAPI(generics.ListAPIView):
    def list(self,request):
        return Response({"Employee":"Mark",
                         "Department": "Accounting"})

class EmployeeCreatedDomains(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        email = self.request.query_params.get('email')
        query = Domain.objects.filter(created_by__email = email)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})


class SubDomainsbyDomain(generics.ListAPIView):
    serializer_class = SubdomainSerializer
    def list(self, request):
        Domain_Name = self.request.query_params.get('Domain_Name')
        query = Subdomain.objects.filter(domain__name__icontains = Domain_Name)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})
    
class DomainsSearch(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        Filter_Name = self.request.query_params.get('Filter_Name')
        Filter_Value = self.request.query_params.get('Filter_Value')
        query_dict = {}
        temp = str(Filter_Name)+'__icontains'
        query_dict[temp] = Filter_Value
        query = Domain.objects.filter(**query_dict)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})

class DomainsFilter(generics.ListAPIView):
    serializer_class = DomainSerializer
    def list(self, request):
        filters = Q()
        name = self.request.query_params.get('name')
        Registrar = self.request.query_params.get('Registrar')
        created_at = self.request.query_params.get('created_at')
        expiry_date = self.request.query_params.get('expiry_date')
        if name:
            filters |= Q(name__icontains=name)
        if Registrar:
            filters |= Q(Registrar__icontains=Registrar)
        if created_at:
            date = datetime.datetime.strptime(created_at, "%Y-%m-%d")
            filters |= Q(created_at__gt=date)
        if expiry_date:
            date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")
            filters |= Q(expiry_date__lt=date)
        query = Domain.objects.filter(filters)
        serializer = self.get_serializer(query,many=True)
        return Response({"result:":serializer.data})