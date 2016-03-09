# -*- coding: utf-8 -*-

from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import DividerPluginModel

class DividerPlugin(CMSPluginBase):
    name = u'Разделитель'
    model = DividerPluginModel
    render_template = 'divider\_divider_plugin.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
            return settings.STATIC_URL + 'divider/images/divider_plugin_icon.png'

    def icon_alt(self, instance):
        return u'Разделитель: %s' % instance

plugin_pool.register_plugin(DividerPlugin)

