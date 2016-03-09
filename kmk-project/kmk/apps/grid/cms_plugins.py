# -*- coding: utf-8 -*-

from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GridPluginModel

class GridPlugin(CMSPluginBase):
    name = u'Изображения (сетка)'
    model = GridPluginModel
    render_template = 'grid\_grid_plugin.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
            return settings.STATIC_URL + 'grid/images/grid_plugin_icon.png'

    def icon_alt(self, instance):
        return u'Изображения (сетка): %s' % instance

plugin_pool.register_plugin(GridPlugin)

