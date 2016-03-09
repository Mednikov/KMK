# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import DetailView

from .models import IndexPage



class IndexDetailView(DetailView):
    model = IndexPage
    context_object_name = 'page'

    # def render_to_response(self, context, **response_kwargs):
        


    #     return super(IndexDetailView, self).render_to_response(context, **response_kwargs)