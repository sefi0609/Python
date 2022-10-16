from django.contrib import admin
from apps.calendar_app.models import Event

# Register model for the admin site
admin.site.register(Event)