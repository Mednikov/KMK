# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

# from .menu import StaffSubMenu


class MapApp(CMSApp):
    name = _('Map')
    urls = ['kmk.apps.map.urls', ]
    app_name = 'map'
    # menus = [StaffSubMenu, ]

apphook_pool.register(MapApp)