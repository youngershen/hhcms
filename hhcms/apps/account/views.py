from hhcms.apps.common.views import View
import logging
logger = logging.getLogger(__name__)


class Register(View):
    http_method_names = ['get', 'post']


class RegisterWithUsername(Register):
    template_name = ''

    def get_context(self, request, *args, **kwargs):
        return self.to_template('')


class Login(View):
    pass


register = Register.as_view()
login = Login.as_view()
