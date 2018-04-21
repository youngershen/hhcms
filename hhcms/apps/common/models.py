from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.


class Model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_('created time'))
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('updated time'))
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name=_('deleted time'))

    @classmethod
    def get_obj_or_none(cls, **kwargs):
        try:
            obj = cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            obj = None
        return obj

    class Meta:
        abstract = True
