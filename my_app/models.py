from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    erp_id = models.CharField(max_length=25,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100, unique=True,blank=True,null=True)
    mobile = models.IntegerField(unique=True,blank=True,null=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
def validate_url(Value):
    url_validator = URLValidator()
    try:
        url_validator(Value)
    except:
        raise ValidationError("Invalid URL")
    
class DomainProvider(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Employee,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Domain(models.Model):
    parent_domain = models.ForeignKey('self',blank=True,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    registrar = models.ForeignKey(DomainProvider,on_delete=models.CASCADE)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    domain_expiry_date = models.DateTimeField(null=True,blank=True)
    certificate_expiry_date = models.DateTimeField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

