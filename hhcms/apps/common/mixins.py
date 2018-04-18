# PROJECT : hhcms
# TIME : 18-4-17 下午4:25
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531


class CommonPermisson:

    def get_permission(self):
        raise NotImplementedError()

    def post_permission(self):
        raise NotImplementedError()

    def check_permission(self):
        return True


class APIPermission(CommonPermisson):

    @staticmethod
    def put_permission():
        return True

    @staticmethod
    def delete_permission():
        return True
