
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MD1(MiddlewareMixin):

    def process_request(self, request):
        print("MD1里面的 process_request")
        

    def process_response(self, request, response):
        print('*'*100)
        print(request.path)
        print('add' in request.path)
        print('*'*100)
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("-" * 80)
    #     print("MD1 中的process_view")
    #     print(view_func, view_func.__name__)





# print("MD1里面的 process_response:")
# print(request.path_info)
# print('*'*100)
# class my_mid(object):
# 	def __init__(self,get_response):
# 		print('--------------init')

# 	def process_request(self,request):
# 		print('--------------request')

# 	# def process_view(self,request, view_func, *view_args, **view_kwargs):
# 	# 	print('--------------view')

# 	# def process_response(self,request, response):
# 	# 	print('--------------response')
# 	# 	return response

# # class my_mid(object):
# #     '''中间件类'''
# #     def __init__(self,get_response):
# #         '''服务器重启之后，接收第一个请求时调用'''
# #         print('----init----')

# class BlockedIPSMiddleware(object):
#     '''中间件类'''
#     EXCLUDE_IPS = ['172.16.179.152']

#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         '''视图函数调用之前会调用'''
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
#             return HttpResponse('<h1>Forbidden</h1>')