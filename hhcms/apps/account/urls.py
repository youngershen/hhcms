# PROJECT : hhcms
# TIME : 18-4-20 下午3:28
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531

from django.urls import path
from hhcms.apps.account.views import \
    register, \
    login, \
    user_exists

app_name = 'account'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('user-exists', user_exists, name='user-exists')
]
