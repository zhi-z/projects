from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class XadminConfig(AppConfig):
    name = 'Xadmin'

    def ready(self):
    	# 实现启动的适加载所有含有Xadmin的插件
    	autodiscover_modules('Xadmin')
