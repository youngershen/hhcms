#!/usr/bin/env python
import os
import sys

path = os.path.abspath('.')
sys.path.append(path)

from hhcms.utils import get_env

env = get_env()

DJANGO_SETTINGS_MODULE = env.str('DJANGO_SETTINGS_MODULE')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)
