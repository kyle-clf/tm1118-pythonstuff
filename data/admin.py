from django.contrib import admin


# import Entry model
from .models import Event


# Register your models here.
admin.site.register(Event)