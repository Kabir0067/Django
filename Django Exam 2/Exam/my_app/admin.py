from django.contrib import admin
from .models import Task, CustUser
from django.contrib.auth.models import Group, User

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'is_done')
    list_filter = ('assigned_to', 'is_done')
    search_fields = ('title', 'description', 'assigned_to__username') 
    fields = ('title', 'description', 'assigned_to', 'is_done')

@admin.register(CustUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    fields = ('username', 'email')

admin.site.unregister(User)
admin.site.unregister(Group)
