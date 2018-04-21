from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from hhcms.apps.common.models import Model

# Create your models here.


class User(AbstractUser, Model):
    username = models.CharField(max_length=150,
                                unique=True,
                                verbose_name=_('username'))

    email = models.EmailField(db_index=True,
                              blank=True,
                              null=True,
                              default='',
                              verbose_name=_('email address'),)

    cellphone = models.CharField(db_index=True,
                                 max_length=255,
                                 blank=True,
                                 null=True,
                                 default='',
                                 verbose_name=_('cellphone number'),)

    EMAIL_FIELD = 'email'
    CELLPHONE_FIELD = 'cellphone'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def text_user(self, message):
        pass

    @classmethod
    def get_cellphone_field_name(cls):
        try:
            return cls.CELLPHONE_FIELD
        except AttributeError:
            return 'email'

    def get_cellphone(self):
        return getattr(self, self.get_cellphone_field_name(), None)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
