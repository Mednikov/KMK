# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import ListView

from .models import StaffMember



class StaffListView(ListView):
    model = StaffMember
    queryset = StaffMember.objects.order_by('seniority').all()

    # def render_to_response(self, context, **response_kwargs):
        


    #     return super(IndexDetailView, self).render_to_response(context, **response_kwargs)