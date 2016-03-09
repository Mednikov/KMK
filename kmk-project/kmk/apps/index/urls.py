# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import IndexDetailView



urlpatterns = patterns('',

    # Detail View
    url(r'^$', IndexDetailView.as_view(), name='index_detail'),
)