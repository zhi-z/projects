from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect

class ModelXadmin(object):
    def __init__(self,model,site):
        self.model = model
        self.site = site

    def list_view(self, request):
        data_list = self.model.objects.all()
        model_name = self.model._meta.model_name

        return render(request,"list_view.html",{'data_list':data_list,"model_name":model_name})

    def add_view(self, request):
        return render(request,"add_view.html")

    def change_view(self, request, id):
        return render(request,"change_view.html")

    def delete_view(self, request, id):
        return render(request,"delete_view.html")


    def get_urls2(self):
        temp = []

        temp.append(url(r"^$", self.list_view))
        temp.append(url(r"^add/$", self.add_view))
        temp.append(url(r"^(\d+)/change/$", self.change_view))
        temp.append(url(r"^(\d+)/delete/$", self.delete_view))
        return temp

    @property
    def urls2(self):

        return self.get_urls2(),None,None

# class XadminSite(object):
#     def __init__(self, name='admin'):
#         self._registry = {}


#     def register(self, model, admin_class=None, **options):
#         if not admin_class:
#                  admin_class = ModelXadmin

#         self._registry[model] = admin_class(model, self) 


class XadminSite(object):
    def __init__(self, name='admin'):
        self._registry = {}


    def get_urls(self):
        print(self._registry)  # {Book:modelAdmin(Book),.......}

        temp = []
        for model, admin_class_obj in self._registry.items():
            app_name = model._meta.app_label
            model_name = model._meta.model_name

            temp.append(url(r'^{0}/{1}/'.format(app_name, model_name), admin_class_obj.urls2), )


            '''
            url(r"app01/book",ModelXadmin(Book,site).urls2)
            url(r"app01/publish",ModelXadmin(Publish,site).urls2)
            url(r"app02/order",ModelXadmin(Order,site).urls2)
            
            '''
        return temp

    @property
    def urls(self):

        return self.get_urls(),None,None

    def register(self, model,admin_class=None, **options):
        if not admin_class:
            admin_class = ModelXadmin

        self._registry[model] = admin_class(model,self)   # {Book:ModelAdmin(Book),Publish:ModelAdmin(Publish)}
        


# 
site = XadminSite()