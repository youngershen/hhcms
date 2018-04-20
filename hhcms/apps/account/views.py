from hhcms.apps.common.views import View


class Register(View):
    http_method_names = ['get']

    def get_context(self, request, *args, **kwargs):
        # return self.to_json({'name': 'fucker', 'id': request.GET.get('id')})
        return self.to_template({})

class Login(View):
    pass


register = Register.as_view()
login = Login.as_view()
