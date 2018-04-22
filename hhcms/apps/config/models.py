from django.db import models
from django.utils.translation import ugettext as _
from hhcms.apps.common.models import Model
# Create your models here.


class Config(Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    value = models.TextField(blank=True, null=True, default='', verbose_name=_('Value'))
    comment = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name=_('Comment'))
