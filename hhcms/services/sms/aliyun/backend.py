# PROJECT : hhcms
# TIME : 18-4-21 下午3:25
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from hhcms.services.sms.BaseBackend import BaseBackend


class Backend(BaseBackend):

    def text(self, number, message):
        pass