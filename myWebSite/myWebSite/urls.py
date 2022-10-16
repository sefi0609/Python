from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.login_app.urls')),
    path('todo_list', include('apps.todo_list_app.urls')),
    path('calendar', include('apps.calendar_app.urls')),
    path('admin/', admin.site.urls),
]