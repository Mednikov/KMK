# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('team', '0004_auto_20160228_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampluginmodel',
            name='photo',
            field=filer.fields.image.FilerImageField(blank=True, null=True, help_text='Optional. Please supply a photo of this staff member.', on_delete=django.db.models.deletion.SET_NULL, to='filer.Image'),
        ),
    ]
