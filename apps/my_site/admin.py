from django.contrib import admin
from apps.my_site.forms import *


class ContactUser(admin.ModelAdmin):
    form = UserCreateForm()
    list_display = '__all__'
