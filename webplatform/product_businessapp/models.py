from __future__ import unicode_literals

from django.db import models
from core.models import TimestampedModel
from business.models import Organization
from customers.models import BaseCustomerApp

from django.contrib.postgres.fields import JSONField


class BusinessApp(BaseCustomerApp):
    """
    Configuration of business app
    many fields are taken from organization, but can be overridden
    using organization_custom_data json field.
    """
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=200)
    version = models.IntegerField(default=1)

    # app assets
    app_icon = models.URLField(null=True, blank=True)
    app_splash = models.URLField(null=True, blank=True)

    # global config. should contain used modules, etc
    app_config = JSONField(null=True, blank=True, default=dict)

    #basic media and copy
    main_logo = models.URLField(null=True, blank=True)
    main_slogan = models.CharField(max_length=300, null=True, blank=True)

    # overrides for organization fields
    organization_custom_data = JSONField(null=True, blank=True, default=dict)

    # app modules config
    features_data = JSONField(null=True, blank=True, default=dict)
    gallery_data = JSONField(null=True, blank=True, default=dict)
    product_data = JSONField(null=True, blank=True, default=dict)
    contact_data = JSONField(null=True, blank=True, default=dict)

    # theme config
    theme_data = JSONField(null=True, blank=True, default=dict)

    # notification stuff: google configs for FCM
    #...
    #...

    class Meta:
        unique_together = ('name', 'version')
