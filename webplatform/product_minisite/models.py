from __future__ import unicode_literals

from django.db import models
from core.models import TimestampedModel
from business.models import Organization
from customers.models import BaseCustomerApp

from django.contrib.postgres.fields import JSONField
#from jsoneditor.fields import JSONSchemaField

import os
import json

#TODO: unused now
with open(os.path.join(os.path.dirname(__file__), "site_config_schema.json")) as fl:
    SITE_CONFIG_SCHEMA = json.load(fl)

from .schemas.theme_data_schema import THEME_DATA_SCHEMA
theme_data_schema = json.loads(THEME_DATA_SCHEMA)

from .schemas.features_data_schema import FEATURES_DATA_SCHEMA
features_data_schema = json.loads(FEATURES_DATA_SCHEMA)


AVAILABLE_TEMPLATES = [
    ('merlin-master', 'merlin-master'),
    ('startbootstrap-grayscale', 'startbootstrap-grayscale'),
]


class MiniSite(BaseCustomerApp):
    """
    Configuration of minisite
    many fields are taken from organization, but can be overridden
    using organization_custom_data json field.
    """
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=200, unique=True)
    #for now, we don't touch version
    version = models.IntegerField(default=1, editable=False)

    #config
    site_template = models.CharField(max_length=200, choices=AVAILABLE_TEMPLATES, default="merlin-master")

    # global config. should contain used modules, etc
    site_config = JSONField(null=True, blank=True, default=dict)

    site_content = JSONField(null=True, blank=True, default=dict)
    site_style = JSONField(null=True, blank=True, default=dict)

    #basic media and copy
    main_logo = models.URLField(null=True, blank=True)
    main_slogan = models.CharField(max_length=300, null=True, blank=True)
    site_favicon = models.URLField(null=True, blank=True)

    # overrides for organization fields
    organization_custom_data = JSONField(null=True, blank=True, default=dict)

    # cookie law stuff ... enable when using cookies
    # cookies_data = JSONField(null=True, blank=True, default=dict)

    # analytics stuff: google configs (or other)
    #...
    #...

    class Meta:
        unique_together = ('name', 'version')
