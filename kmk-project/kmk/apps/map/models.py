# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# from adminsortable.models import Sortable
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField



class MapPoint(models.Model):
    class Meta:
        app_label = 'map'

    name = models.CharField(
        u'name',
        blank=False,
        default='',
        help_text=u'Please enter an organisation name',
        max_length=140,
    )

    address = models.CharField(
        u'address',
        blank=False,
        default='',
        help_text=u'Please enter a contact adress',
        max_length=140,
    )

    lat = models.CharField(
        u'latitude',
        blank=False,
        default='',
        help_text=u'Please enter a latitude',
        max_length=16,
    )

    lon = models.CharField(
        u'longitude',
        blank=False,
        default='',
        help_text=u'Please enter a longitude',
        max_length=16,
    )

    def get_absolute_url(self):
        return reverse('map:map', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.name