# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField



class MediaPluginModel(CMSPlugin):

    heading = models.CharField(
        u'heading',
        blank=False,
        default='',
        help_text=u'Please enter a heading for this post',
        max_length=120,
    )

    heading_link = models.CharField(
        u'heading link',
        blank=True,
        default='',
        help_text=u'Please enter a heading link for this post (example http:\\\google.ru)',
        max_length=200,
    )

    image = FilerImageField(
        blank=True,
        help_text=u'Please supply an image of this post',
        null=True,
        on_delete=models.SET_NULL,  # Important
    )

    description = models.TextField(
        'description',
        blank=True,
        default='',
        help_text=u'Please enter a description for this post',
        max_length=300,
    )

    def __str__(self):
        return u'%s' % (self.heading,)
