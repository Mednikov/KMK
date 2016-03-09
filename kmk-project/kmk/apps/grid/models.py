# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField



class GridPluginModel(CMSPlugin):

    alt = models.CharField(
        u'alt',
        blank=True,
        default='',
        help_text=u'Optional. Please enter an alternative text for image',
        max_length=120,
    )

    img = FilerImageField(
        blank=False,
        help_text=u'Please supply an image.',
        null=True,
        on_delete=models.SET_NULL,  # Important
    )

    url = models.CharField(
        u'URL',
        blank=True,
        default='',
        help_text=u'Optional. Please enter an URL for this image (example: http://ya.ru)',
        max_length=200,
    )

    def __str__(self):
        return u'%s' % (self.alt,)
