# PROJECT : hhcms
# TIME : 18-4-21 下午3:25
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531

from abc import abstractmethod


class BaseBackend:

    @abstractmethod
    def text(self, number, message):
        pass