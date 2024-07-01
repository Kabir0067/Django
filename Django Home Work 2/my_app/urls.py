from django.urls import path
from .views import *

urlpatterns=[
    path('home', hom_page ),
    path('about', about_page)
]