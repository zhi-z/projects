from Xadmin.service.Xadmin import site


print('app02 Xadmin')

from app02.models import *

site.register(Order)
site.register(Food)

print("_registry:  ",site._registry)
