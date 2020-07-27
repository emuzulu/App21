from django.contrib import admin
from .models import Application
from django.contrib.auth.models import User


# Register your models here.

class AppAdmin(admin.ModelAdmin):
    list_display = ('id', "company", "role", 'user')


admin.site.register(Application, AppAdmin)
