
from Xadmin.service.Xadmin import site


print('app01 Xadmin')

from app01.models import *

site.register(Book)
site.register(Publish)
site.register(Author)
site.register(AuthorDetail)