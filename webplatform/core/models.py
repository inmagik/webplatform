from __future__ import unicode_literals

from django.db import models

class TimestampedModel(models.Model):
    """
    Base model with timestamps
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
