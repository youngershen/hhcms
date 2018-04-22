# PROJECT : hhcms
# TIME : 18-4-16 下午4:14
# AUTHOR : Younger Shen
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
import os
import environ
from datetime import datetime


def get_base_path():
    path = environ.Path(__file__)
    base_dir = path - 3
    return str(base_dir)


def get_env(file_name='.env'):
    env = environ.Env()
    abs_path = get_base_path()
    env_path = os.path.join(abs_path, file_name)
    env.read_env(env_path)
    return env


def get_log_path():
    env = get_env()
    path = env.str('LOG_DIR')
    if not path.startswith('/'):
        path = os.path.join(get_base_path(), path)

    return path


def get_log_file():
    now = datetime.utcnow()
    path = get_log_path()
    path = os.path.join(path, now.strftime('%Y/%m'))

    if not os.path.exists(path):
        os.makedirs(path)

    return os.path.join(path, now.strftime('%d.log'))



