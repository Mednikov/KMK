# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20160222_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffmember',
            old_name='full_name',
            new_name='name',
        ),
    ]
