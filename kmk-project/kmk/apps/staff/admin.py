from django.contrib import admin

# Register your models here.
from .models import StaffMember, Seniority


class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(StaffMember, StaffAdmin)


class SeniorityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Seniority, SeniorityAdmin)