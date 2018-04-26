# PROJECT : hhcms
# TIME : 18-4-22 下午9:35
# AUTHOR : 申延刚 <Younger Shen>
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.utils.translation import ugettext as _
from validator import Validator


class Register(Validator):
    username = 'required|min_length:4'
    email = 'required|email'
    password = 'required|min_length:8'

    message = {
        'username': {
            'required': _('username is required'),
            'min_length': _('username is shorter than 4')
        },
        'email': {
            'required': _('email is required'),
            'email': _('invalid email address')
        },
        'password': {
            'required': _('password is required'),
            'min_length': _('password is shotter than 8')
        }
    }
