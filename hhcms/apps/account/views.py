import logging
from django.db.models.query import Q
from hhcms.apps.common.views import View as BaseView
from hhcms.apps.common.mixins import Config
from hhcms.apps.account.validators import Register as RegisterValidator
from hhcms.apps.account.models import User
logger = logging.getLogger(__name__)


class View(Config, BaseView):
    pass


class Index(View):
    http_method_names = ['get', 'post']
    template_name = 'index.html'


class Register(View):
    template_name = 'register.html'

    def get_context(self, request, *args, **kwargs):
        message = self.get_message()
        data = self.get_config()
        data.update(**message)
        return self.to_template(data)

    def post_context(self, request, *args, **kwargs):
        validator = RegisterValidator(request.POST)
        validator.validate()
        if validator.status:
            logger.debug(request.POST)
            message = {'ok': 'cool'}
        else:
            message = validator.get_message()
            message_plain = validator.get_message_plain()
            logger.debug(message_plain)

        return self.redirect(message=message_plain)

    def get_redirect_url(self, *args, **kwargs):
        return '/account/register'


class Login(View):
    template_name = 'login.html'

    def get_context(self, request, *args, **kwargs):
        data = self.get_config()
        return self.to_template(data)

    def post_context(self, request, *args, **kwargs):
        return self.redirect('/')


class UserExists(BaseView):
    http_method_names = ['post']

    def post_context(self, request, *args, **kwargs):
        username, email = self.get_payload(request)
        r = self.user_exists(username, email)
        return self.to_json({'status': r})

    @staticmethod
    def get_payload(request):
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        return username, email

    @staticmethod
    def user_exists(username, email):
        if username or email:
            query = Q(username=username) | Q(email=email)
            users = User.objects.filter(query)
            return True if users else False
        else:
            return False


register = Register.as_view()
login = Login.as_view()
user_exists = UserExists.as_view()
