from django.urls import path

from .views import *
urlpatterns = [
    path('employee/',EmployeeView.as_view()),
    path('domain/',DomainView.as_view()),
    path('domainprovider/',DomainProviderView.as_view()),

    path('alldomains/',AllDomains.as_view()),

    path('allSubdomains/',AllSubdomains.as_view()),

    path('subdomainsbydomain/',SubdomainsbyDomains.as_view()),

    path('domainsearch/',DomainsSearch.as_view()),

    path('domainfilter/',DomainsFilter.as_view()),

    path('subdomainsearch/',SubDomainsSearch.as_view()),

    path('subdomainfilter/',SubDomainsFilter.as_view()),
]