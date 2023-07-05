from django.urls import path
# from .views import EmployeeCreate, EmployeeList, EmployeeUpdate, EmployeeDelete
# from .views import EmployeeView, DomainView, SubdomainView
# from .views import DomainCreate, DomainList, DomainUpdate, DomainDelete
# from .views import SubDomainCreate, SubDomainList, SubDomainUpdate, SubDomainDelete, 
# from .views import EmployeeCreatedDomains, DomainsSearch, DomainsFilter, SubDomainsbyDomain
from .views import *
urlpatterns = [
    # path('Employee/create',EmployeeCreate.as_view()),
    # path('Employee/list',EmployeeList.as_view()),
    # path('Employee/update/<int:pk>',EmployeeUpdate.as_view()),
    # path('Employee/delete/<int:pk>',EmployeeDelete.as_view()),
    path('Employee/',EmployeeView.as_view()),
    path('Domain/',DomainView.as_view()),
    path('Subdomain/',SubdomainView.as_view()),
    # path('Domain/create/',DomainCreate.as_view()),
    # path('Domain/list/',DomainList.as_view()),
    # path('Domain/update/<int:pk>',DomainUpdate.as_view()),
    # path('Domain/delete/<int:pk>',DomainDelete.as_view()),
    path('TestApi/',TestAPI.as_view()),
    # path('SubDomain/create/',SubDomainCreate.as_view()),
    # path('SubDomain/list/',SubDomainList.as_view()),
    # path('SubDomain/update/<int:pk>',SubDomainUpdate.as_view()),
    # path('SubDomain/delete/<int:pk>',SubDomainDelete.as_view()),

    path('Domain/ECD/',EmployeeCreatedDomains.as_view()),

    path('Domain/DomainsSearch/',DomainsSearch.as_view()),

    path('Domain/DomainsFilter/',DomainsFilter.as_view()),

    path('SubDomain/SBD/',SubDomainsbyDomain.as_view()),
]
