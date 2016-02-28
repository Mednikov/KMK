# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TeamPluginModel

class TeamPlugin(CMSPluginBase):
    name = u'Сотрудники (сетка)'
    model = TeamPluginModel
    render_template = 'team\_team_plugin.html'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TeamPlugin)

