# -*- coding: utf-8 -*-
from django.db import models
# from django.core.urlresolvers import reverse



class IndexPage(models.Model):
    class Meta:
        app_label = 'index'

    title = models.CharField(
        u'Заголовок',
        blank=False,
        default='',
        help_text=u'Введите заголовок страницы',
        max_length=80,
    )

    description = models.TextField(
        u'Описание',
        blank=False,
        default='',
        help_text=u'Введите описание страницы',
        max_length=200,
    )

    def __unicode__(self):
        return self.title