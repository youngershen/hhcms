# PROJECT : hhcms
# TIME : 18-4-22 下午3:16
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.test import TestCase
from hhcms.utils.config import set_config, get_config
from hhcms.apps.config.exceptions import ConfigNameHadExists


class Util(TestCase):
    def setUp(self):
        self.name = 'test_name'
        self.value = 'test_value'

    def set_config(self):
        r = set_config(self.name, self.value)
        self.assertTrue(r)

        value = get_config(self.name)
        self.assertEqual(value, self.value)
        try:
            set_config(self.name, value)
        except Exception as e:
            self.assertIsInstance(e, ConfigNameHadExists)

        r = set_config(self.name, value, safe=False)
        self.assertTrue(r)

    def get_config(self):
        value = get_config(self.name)
        self.assertEqual(value, self.value)