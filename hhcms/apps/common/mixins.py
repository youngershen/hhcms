# PROJECT : hhcms
# TIME : 18-4-17 下午4:25
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from abc import ABC, abstractmethod


class CommonPermisson(ABC):

    @abstractmethod
    def get_permission(self):
        pass

    @abstractmethod
    def post_permission(self):
        pass

    def check_permission(self):
        pass


class APIPermission(CommonPermisson):

    @abstractmethod
    def put_permission(self):
        pass

    @abstractmethod
    def delete_permission(self):
        pass

    @abstractmethod
    def patch_permission(self):
        pass

    @abstractmethod
    def head_permission(self):
        pass

    @abstractmethod
    def options_permission(self):
        pass

    @abstractmethod
    def trace_permission(self):
        pass
