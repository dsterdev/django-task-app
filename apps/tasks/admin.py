from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'important', 'date_completed']
    readonly_fields = ['created_at']
