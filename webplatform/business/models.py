from __future__ import unicode_literals

from django.db import models
from customers.models import BaseCustomerModel


class Organization(BaseCustomerModel):

    name =  models.CharField(max_length=200)
    code =  models.CharField(max_length=200, unique=True)

    city = models.CharField(max_length=200, null=True, blank=True)
    province = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(null=True, blank=True)


    def __unicode__(self):
        return u'%s' % self.code
