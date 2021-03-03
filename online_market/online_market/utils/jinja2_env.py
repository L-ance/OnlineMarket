# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 1:25 下午
# @Author  : 熊礼俊
# @File    : jinja2_env.py
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env
