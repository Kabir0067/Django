from django.urls import path
from .views import *

urlpatterns=[
    path('home', hom_page ,name='home'),
    path('about', about_page,name='about')
]