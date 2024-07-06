from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_users, name='read_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  

]
