from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'avatar',
        'about',
        'birth_date',
        'phone',
        'city',
        'gender',


    ]
# Register your models here.
