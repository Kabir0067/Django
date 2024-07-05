from django.urls import path
from .views import home_page,user_page

urlpatterns=[
    path('home', home_page),
    path('user',user_page)
]