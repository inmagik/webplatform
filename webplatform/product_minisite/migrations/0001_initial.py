# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 01:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('customer_is_admin', models.BooleanField(default=True)),
                ('customer_is_publisher', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('version', models.IntegerField(default=1)),
                ('site_favicon', models.URLField(blank=True, null=True)),
                ('site_config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('main_logo', models.URLField(blank=True, null=True)),
                ('main_slogan', models.CharField(blank=True, max_length=300, null=True)),
                ('organization_custom_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('features_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('contact_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('theme_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Organization')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='minisite',
            unique_together=set([('name', 'version')]),
        ),
    ]