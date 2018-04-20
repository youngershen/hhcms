from django.views.generic import View as DjangoView
from django.views.generic.base import TemplateResponseMixin
from hhcms.apps.common.mixins import Permisson, \
    APIPermission, \
    Context, \
    APIContext, \
    Response, \
    RedirectResponse


class View(Context, Permisson, Response, TemplateResponseMixin, RedirectResponse, DjangoView):
    template_name = 'default/index.html'
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_context(self):
        pass

    def post_context(self):
        pass

    def put_context(self):
        pass

    def delete_context(self):
        pass


class API(APIContext, APIPermission, View):
    http_method_names = ['get', 'post', 'put', 'delete']

    def patch_context(self):
        pass

    def head_context(self):
        pass

    def options_context(self):
        pass

    def trace_context(self):
        pass


class Handler404(View):
    pass


class Handler500(View):
    pass


class Handler405(View):
    pass
