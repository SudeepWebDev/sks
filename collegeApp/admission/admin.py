from django.contrib import admin
from .models import UserLoginDetails
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("email","password")
admin.site.register(UserLoginDetails, UserAdmin)