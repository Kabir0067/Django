from django.shortcuts import render,HttpResponse

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')