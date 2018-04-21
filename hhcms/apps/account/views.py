from hhcms.apps.common.views import View
import logging
logger = logging.getLogger(__name__)
print(__name__)


class Register(View):
    http_method_names = ['get']

    def get_context(self, request, *args, **kwargs):
        # return self.to_json({'name': 'fucker', 'id': request.GET.get('id')})
        logger.debug('tessfsdft test')
        return self.to_template({})


class Login(View):
    pass


register = Register.as_view()
login = Login.as_view()
