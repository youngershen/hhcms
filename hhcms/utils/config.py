# PROJECT : hhcms
# TIME : 18-4-22 下午3:07
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.utils.translation import ugettext as _
from hhcms.apps.config.models import Config
from hhcms.apps.config.exceptions import ConfigNameHadExists


def get_config(name, default=None):
    record = Config.get_obj_or_none(name=name)
    return record.value if record else default


def set_config(name, value, safe=True):
    record = Config.get_obj_or_none(name=name)

    if record:
        if safe:
            raise ConfigNameHadExists(_('the record of name : {NAME} had exists in the config table, if you'
                                        ' still want to set the value, please set safe to False.'
                                        .format(NAME=name)))
        else:
            record.value = value
            record.save()
    else:
        Config.objects.create(name=name, value=value)

    return True
