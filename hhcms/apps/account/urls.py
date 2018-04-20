# PROJECT : hhcms
# TIME : 18-4-20 下午3:28
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531

from django.urls import path
from hhcms.apps.account.views import register, login

urlpatterns = [
    path('register', register, name='account-register'),
    path('login', login, name='account-login')
]
