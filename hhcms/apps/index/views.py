from hhcms.apps.common.views import View
from hhcms.apps.common.mixins import Config


class Index(Config, View):
    http_method_names = ['get']
    template_name = 'index.html'

    def get_context(self, request, *args, **kwargs):
        data = self.get_config()
        return self.to_template(data)


index = Index.as_view()
