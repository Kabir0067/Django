from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def hom_page(request):
    return render(request, 'index.html' )

def about_page(request):
    return render(request, 'about.html'     )
