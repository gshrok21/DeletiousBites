from django.contrib import admin
from menu.models import menu_des

# Register your models here.
class menu_admin(admin.ModelAdmin):
    list_menu=('title','price','about','ingredients','badge','variant')
admin.site.register(menu_des,menu_admin)