from django.contrib import admin
from.models import CustomUser,Tasks

admin.site.register([CustomUser,Tasks])
