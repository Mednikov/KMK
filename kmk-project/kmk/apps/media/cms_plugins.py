# -*- coding: utf-8 -*-

from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import MediaPluginModel

class MediaPlugin(CMSPluginBase):
    name = u'Пост'
    model = MediaPluginModel
    render_template = 'media\_media_plugin.html'
    # text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(MediaPlugin)

