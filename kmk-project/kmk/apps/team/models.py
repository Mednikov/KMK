# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin
# from kmk.apps.staff.models import Seniority
from filer.fields.image import FilerImageField



class TeamPluginModel(CMSPlugin):

    full_name = models.CharField(
        u'full name',
        blank=False,
        default='',
        help_text=u'Please enter a full name for this staff member',
        max_length=64,
    )

    seniority = models.CharField(
        u'seniority',
        blank=True,
        default='',
        help_text=u'Please specify a seniority level for this staff member',
        max_length=64,
    )

    # seniority = models.ForeignKey(
    #     'staff.Seniority',
    #     blank=True,
    #     default=None,
    #     help_text=u'Please specify a seniority level for this staff member',
    #     null=True
    # )

    photo = FilerImageField(
        blank=True,
        help_text=u'Optional. Please supply a photo of this staff member.',
        null=True,
        on_delete=models.SET_NULL,  # Important
    )

    email = models.CharField(
        u'e-mail',
        blank=True,
        default='',
        help_text=u'Please enter an e-mail for this staff member',
        max_length=64,
    )

    phone = models.CharField(
        u'phone',
        blank=True,
        default='',
        help_text=u'Please enter a phone number for this staff member',
        max_length=64,
    )

    bio = models.TextField(
        'staff_bio',
        blank=True,
        default='',
        help_text=u'Please enter a bio for this staff member',
        max_length=300,
    )

    def __str__(self):
        return u'%s' % (self.full_name,)
