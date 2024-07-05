from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def user_page(request):
    user_data={
        'name': 'kabir',
        'surname':'gafurov',
        'user_name':'gafurov0067',
        'age':18}
    return render(request, 'about.html', context=user_data)

