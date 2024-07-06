from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser

def read_users(request):
    users = CustomUser.objects.all()
    return render(request, 'index.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        age = request.POST['age']
        address = request.POST['address']  
        email = request.POST['email']
        phone_number = request.POST['phone_number']  

        model = CustomUser(first_name=fname,
                           last_name=lname,
                           user_name=uname,
                           age=age,
                           address=address,
                           email=email,
                           phone_number=phone_number)

        model.save()
        return redirect('read_users')  
    return render(request, 'create_user.html')

def update_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.user_name = request.POST['uname']
        user.age = request.POST['age']
        user.address = request.POST['address']
        user.email = request.POST['email']
        user.phone_number = request.POST['phone_number']  
        user.save()
        return redirect('read_users') 
    return render(request, 'update_user.html', {'user': user})



def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('read_users')
    return render(request, 'delete_user.html', {'user': user})