from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import CustomUser, Tasks

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(CustomUser)
admin.site.register(Tasks)
