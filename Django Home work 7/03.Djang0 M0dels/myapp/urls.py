from django.urls import path
from . import views


urlpatterns = [
    # path('home',views.home_page),
    # path("about",views.about)
    path('list',views.news_home,name="list-page"),    
]