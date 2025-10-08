from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(todoModel)
class todoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'descrition', 'created_at', 'updated_at']