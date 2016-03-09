# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import StaffListView



urlpatterns = patterns('',

    # List View
    url(r'^$', StaffListView.as_view(), name="staffmember_list"),
)