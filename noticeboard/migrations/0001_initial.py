# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create_event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=20)),
                ('date_time', models.DateField()),
                ('seats', models.IntegerField(default=200)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_instructions', models.CharField(max_length=500)),
                ('option_website_link', models.CharField(max_length=100)),
                ('option_contact_info', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
