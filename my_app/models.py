from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ERP_ID = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.IntegerField(unique=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.email

def validate_url(Value):
    url_validator = URLValidator()
    try:
        url_validator(Value)
    except:
        raise ValidationError("Invalid URL")



class Domain(models.Model):
    # parent_domain = models.ForeignKey('self',blank=True,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    Registrar = models.CharField(max_length=200)
    # IP_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    domain_expiry_date = models.DateTimeField(null=True,blank=True)
    certificate_expiry_date = models.DateTimeField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Subdomain(models.Model):
    Subdomain_name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    domain = models.ForeignKey(Domain,on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    domain_expiry_date = models.DateTimeField(null=True,blank=True)
    certificate_expiry_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.sub_name






