from hhcms.apps.common.views import View
import logging
logger = logging.getLogger(__name__)


class RegisterWithUsername(View):

    def get_context(self, request, *args, **kwargs):
        return self.to_template({})


class LoginWithUsername(View):
    pass


register = RegisterWithUsername.as_view()
login = LoginWithUsername.as_view()
