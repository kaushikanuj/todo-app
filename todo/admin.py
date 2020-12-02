from django.contrib import admin
from .models import TodoApp


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'roll_no']


admin.site.register(TodoApp, TodoAdmin)
