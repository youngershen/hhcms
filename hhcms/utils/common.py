# PROJECT : hhcms
# TIME : 18-4-16 下午4:14
# AUTHOR : Younger Shen
# EMAIL : younger.shen@hotmail.com
# CELL : 13811754531
# WECHAT : 13811754531
import os
import environ


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
