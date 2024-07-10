from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, CustUser

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'assigned_to', 'is_done']
    success_url = reverse_lazy('task-list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'assigned_to', 'is_done']
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

class UserListView(ListView):
    model = CustUser
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = CustUser
    template_name = 'user_detail.html'
