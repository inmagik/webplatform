from __future__ import unicode_literals

from django.db import models
from core.models import TimestampedModel
from django.conf import settings


class Customer(TimestampedModel):
    """
    A customer.
    Will have many apps or services purchased.
    Will have many users that can administer or see customer data
    """
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)


class CustomerUser(TimestampedModel):
    """
    User to customer relation
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    customer = models.ForeignKey(Customer)
