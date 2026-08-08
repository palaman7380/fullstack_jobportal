from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'roll']
    list_filter = ['roll']


admin.site.register(CustomUser, CustomUserAdmin)

