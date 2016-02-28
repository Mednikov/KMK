# -*- coding: utf-8 -*-

from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TeamPluginModel

class TeamPlugin(CMSPluginBase):
    name = u'Сотрудники (сетка)'
    model = TeamPluginModel
    render_template = 'team\_team_plugin.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
            return settings.STATIC_URL + 'team/images/team_plugin_icon.png'

    def icon_alt(self, instance):
        return u'Сотрудники (сетка): %s' % instance

plugin_pool.register_plugin(TeamPlugin)

