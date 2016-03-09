# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seniority',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('label', models.CharField(default='', unique=True, help_text='Please provide a label for this seniority', verbose_name='label', max_length=64)),
            ],
            options={
                'verbose_name_plural': 'seniorities',
            },
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('full_name', models.CharField(default='', unique=True, help_text='Please enter a full name for this staff member', verbose_name='full name', max_length=64)),
                ('slug', models.SlugField(default='', help_text='Provide a unique slug for this staff member', verbose_name='slug', max_length=64)),
                ('bio', cms.models.fields.PlaceholderField(slotname='staff_bio', editable=False, null=True, to='cms.Placeholder')),
                ('photo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, help_text='Optional. Please supply a photo of this staff member.', to='filer.Image')),
                ('seniority', models.ForeignKey(to='staff.Seniority', null=True, blank=True, help_text='Please specify a seniority level for this staff member', default=None)),
            ],
        ),
    ]
