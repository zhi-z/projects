
from Xadmin.service.Xadmin import site
from Xadmin.service.Xadmin import ModelXadmin


print('app01 Xadmin')

from app01.models import *

class BookConfig(ModelXadmin):
    list_display = ["title","prcie"]


site.register(Book,BookConfig)
site.register(Publish)
site.register(Author)
site.register(AuthorDetail)