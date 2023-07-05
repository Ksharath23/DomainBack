from django.contrib import admin
from .models import Employee, Domain, Subdomain

admin.site.register(Employee)
admin.site.register(Domain)
admin.site.register(Subdomain)