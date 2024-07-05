from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
]
