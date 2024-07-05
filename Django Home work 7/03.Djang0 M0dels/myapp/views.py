from django.shortcuts import render,HttpResponseRedirect
from .models import Tasks
def news_home(request):
    news=Tasks.objects.all()
    return render(request,"Task.html",{'news': news})


# def task_create(request):
    
#     if request.method=="post":
#         model=Tasks
#         model.title=request.POST.get("title")
#         model.due_date=request.POST.get("due_date")
        

#         model.save()
        
    
#     return

#         # return HttpResponseRedirect("list-page")