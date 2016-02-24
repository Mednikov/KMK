from django.contrib import admin

# Register your models here.
from .models import MapPoint


class MapAdmin(admin.ModelAdmin):
    pass

admin.site.register(MapPoint, MapAdmin)
