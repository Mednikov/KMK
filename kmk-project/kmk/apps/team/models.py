# -*- coding: utf-8 -*-

from django.db import models

from cms.models import CMSPlugin



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
        blank=False,
        default='',
        help_text=u'Please enter a full name for this staff member',
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
        return u'%s:%s:%s' % (self.full_name, self.seniority, self.bio, )
