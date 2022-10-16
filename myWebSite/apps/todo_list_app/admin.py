from django.contrib import admin
from apps.todo_list_app.models import ToDoItem, ToDoList

# Register models for the admin site
admin.site.register(ToDoItem)
admin.site.register(ToDoList)