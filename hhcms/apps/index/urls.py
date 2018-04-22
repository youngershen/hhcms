# PROJECT : hhcms
# TIME : 18-4-22 下午5:42
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.urls import path
from hhcms.apps.index.views import index

urlpatterns = [
    path('', index, name='index-index'),
]
