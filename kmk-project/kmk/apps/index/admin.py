# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import IndexPage



class IndexPageAdmin(admin.ModelAdmin):
    pass

admin.site.register(IndexPage, IndexPageAdmin)


# class ClippingInline(SortableTabularInline):    
#     extra = 1
#     form = select2_modelform(Clipping, attrs={'width': '250px'})
#     model = Clipping


# class IndexPageAdmin(PlaceholderAdminMixin, SortableAdmin):
#     form = select2_modelform(StaffMember, attrs={'width': '250px'})
#     inlines = [ ClippingInline, ]

# admin.site.register(StaffMember, StaffMemberAdmin)