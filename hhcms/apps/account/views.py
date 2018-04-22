import logging
from hhcms.apps.common.views import View as BaseView
from hhcms.apps.common.mixins import Config
logger = logging.getLogger(__name__)


class View(Config, BaseView):
    pass


class Register(View):
    template_name = 'register.html'

    def get_context(self, request, *args, **kwargs):
        data = self.get_config()
        logger.debug(data)
        return self.to_template(data)

    def post_context(self, request, *args, **kwargs):
        return self.redirect('/')


class Login(View):
    pass


register = Register.as_view()
login = Login.as_view()
