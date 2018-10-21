from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from hhcms.apps.common.models import Model

# Create your models here.


class Manager(UserManager):
    pass


class User(AbstractUser, Model):
    username = models.CharField(max_length=100,
                                unique=True,
                                verbose_name=_('Username'))

    email = models.EmailField(unique=True,
                              null=True,
                              verbose_name=_('Email'), )

    cellphone = models.CharField(max_length=100,
                                 unique=True,
                                 null=True,
                                 verbose_name=_('Cellphone'), )

    property = models.


    USERNAME_FIELD = 'username'

    objects = Manager()

    def get_username_field(self):
        return self.USERNAME_FIELD

    def email_user(self, subject, message, from_email=None, **kwargs):
        pass

    def text_user(self):
        pass

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class InfoRecord(Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='info_records',
                             related_query_name='info')

    name = models.CharField(max_length=255,
                            db_index=True,
                            verbose_name=_('Name'))

    value = models.CharField(max_length=255,
                             blank=True,
                             null=True,
                             verbose_name=_('Value'))

    class Meta:
        ordering = ['id']
        verbose_name = _('Info Record')
        verbose_name_plural = _('Info Records')
