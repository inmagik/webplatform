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

    def __unicode__(self):
        return u'%s' % self.code


class CustomerUser(TimestampedModel):
    """
    User to customer relation
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="customer_user")
    customer = models.ForeignKey(Customer)

class BaseCustomerModel(TimestampedModel):
    """
    """
    # customer is nullable so we can easily detach administration and access
    # without losing data.
    customer = models.ForeignKey(Customer, null=True, blank=True)


class BaseCustomerApp(TimestampedModel):
    """
    Base model for apps and services
    """
    # customer is nullable so we can easily detach administration and access
    # without losing data.
    customer = models.ForeignKey(Customer, null=True, blank=True)

    # specify if customer publishes and/or administers app
    # these fields should not be editable by customer
    customer_is_admin = models.BooleanField(default=True)
    customer_is_publisher = models.BooleanField(default=True)


    class Meta:
        abstract = True
