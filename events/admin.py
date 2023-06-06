from django.contrib import admin

# Register your models here.
from .models import Event, KnownOrganizer

admin.site.register(Event)
admin.site.register(KnownOrganizer)