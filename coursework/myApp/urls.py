"""
URL configuration for coursework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.category_products, name='category_products'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('production/', views.production, name='production'),
    path('payment_delivery/', views.payment_delivery, name='payment_delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('portfolio/umschool/', views.project_umschool, name='project_umschool'),
    path('portfolio/digitalskills/', views.project_digitalskills, name='project_digitalskills'),
    path('portfolio/fifa/', views.project_fifa, name='project_fifa'),
    path('portfolio/sport/', views.project_sport, name='project_sport'),
    path('portfolio/tatmedia/', views.project_tatmedia, name='project_tatmedia'),
    path('portfolio/volunteer/', views.project_volunteer, name='project_volunteer'),
]
