import os
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View as DjangoView
from django.views.generic.base import TemplateResponseMixin
from hhcms.apps.common.mixins import Permisson, \
    APIPermission, \
    Context, \
    APIContext, \
    Response, \
    RedirectResponse
from hhcms.utils.config import get_config


class View(Context, Permisson, Response, TemplateResponseMixin, RedirectResponse, DjangoView):
    http_method_names = ['get', 'post', 'put', 'delete']
    template_name = 'index.html'

    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        theme = get_config('theme', default='default')
        name = os.path.join(theme, self.template_name)

        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            return [name]

    def get_context(self, request, *args, **kwargs):
        pass

    def post_context(self, request, *args, **kwargs):
        pass

    def put_context(self, request, *args, **kwargs):
        pass

    def delete_context(self, request, *args, **kwargs):
        pass


class API(APIContext, APIPermission, View):
    http_method_names = ['get', 'post', 'put', 'delete']

    def patch_context(self, request, *args, **kwargs):
        pass

    def head_context(self, request, *args, **kwargs):
        pass

    def options_context(self, request, *args, **kwargs):
        pass

    def trace_context(self, request, *args, **kwargs):
        pass


class Handler404(View):
    pass


class Handler500(View):
    pass


class Handler405(View):
    pass
