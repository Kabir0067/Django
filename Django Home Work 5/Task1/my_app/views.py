from django.shortcuts import render
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'index.html', {'authors': authors})
