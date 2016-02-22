# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=80, help_text='Введите заголовок страницы', default='', verbose_name='Заголовок')),
                ('description', models.TextField(max_length=200, help_text='Введите описание страницы', default='', verbose_name='Описание')),
            ],
        ),
    ]
