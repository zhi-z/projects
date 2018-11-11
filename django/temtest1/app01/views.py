from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Customer,Apps,DeviceAppUpdate
from rest_framework.response import Response

from rest_framework import viewsets
from app01.serilizer import DeviceAppUpdateSerializers
import requests
import re
						

def get_customer(customer_url):
	base_url = 'http://localhost:8000'
	url = base_url  + customer_url;
	ret = requests.get(url)
	j_data = ret.json()
	return j_data

def save_data(objs_data):
	for obj_data in objs_data:
		uids = obj_data['UIDs']
		customer_url = obj_data['customer']
		customer_jdata = get_customer(customer_url)
		customer_name = customer_jdata['name']

		uid_list = uids.split('\r\n')
		if len(uid_list[0]) > 25:
			uid_list = uids.split(' ')

		if uid_list[-1] == '': 
			uid_list.pop()
		# 查看客户是否存在，不存在则先创建客户
		lenght = len(Customer.objects.filter(name = customer_name))
		if  lenght == 0:  
			Customer.objects.create(name = customer_name)

		customer_obj = Customer.objects.get(name = customer_name) 
		for uid in uid_list:
			if  len(DeviceAppUpdate.objects.filter(UID = uid)) == 0:  
				   
				DeviceAppUpdate.objects.create(UID = uid,customer = customer_obj)


def index(request):
	base_url = 'http://localhost:8000'
	url = base_url + '/sellrec/api/query/'
	ret = requests.get(url)
	j_data = ret.json()
	objs_data = j_data['objects']
	meta = j_data['meta']
	meta_offset = meta['offset']
	meta_next = meta['next']
	meta_total_count = meta['total_count']

	save_data(objs_data)

					
	while(meta['next'] != None):
		url = base_url + meta['next']
		ret = requests.get(url)
		j_data = ret.json()
		objs_data = j_data['objects']
		save_data(objs_data)
		
		meta = j_data['meta']
		meta_next = meta['next']

	return HttpResponse('ok.....')


# class Per(object):
#     def has_permission(self):
#         if 1:
#             return
#         else:

    	# authentication_classes = [Per,]	        return


class DeviceAppUpdateModelView(viewsets.ModelViewSet):
	queryset = DeviceAppUpdate.objects.all()
	serializer_class = DeviceAppUpdateSerializers

	# def create(self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.perform_create(serializer)
	# 	headers = self.get_success_headers(serializer.data)
	# 	return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    




