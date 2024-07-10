from django.contrib import admin
from .models import Ctegotiya, Product
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Ctegotiya)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "color", "quantity", "catigoriya"]
    search_fields = ["name",'price']
    list_filter = ["price", "catigoriya", "color"]


