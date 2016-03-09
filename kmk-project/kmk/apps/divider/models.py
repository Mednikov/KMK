# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin
# from kmk.apps.staff.models import Seniority
from filer.fields.image import FilerImageField



class DividerPluginModel(CMSPlugin):

    height = models.CharField(
        u'height',
        blank=False,
        default='',
        help_text=u'Please enter a height for this divider with measure (example: 100px)',
        max_length=8,
    )


    def __str__(self):
        return u'%s' % (self.height,)
