# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import MapListView



urlpatterns = patterns('',

    # List View
    url(r'^$', MapListView.as_view(), name="map_list"),
)