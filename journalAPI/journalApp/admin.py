from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(journalModel)
class journalAdmin(admin.ModelAdmin):
    list_display= ['id','user', 'title', 'content','is_private', 'created_at', 'updated_at']