# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView

from .models import MapPoint



class MapListView(ListView):
    model = MapPoint
    queryset = MapPoint.objects.order_by('lat').all()

    # def render_to_response(self, context, **response_kwargs):
        


    #     return super(IndexDetailView, self).render_to_response(context, **response_kwargs)