from django.contrib import admin
from .models import Readings

class ReadingsAdmin(admin.ModelAdmin):
    fields=('meter','time','rate','total')

admin.site.register(Readings,ReadingsAdmin)