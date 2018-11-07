from django.shortcuts import render
from django.http import HttpResponse
from app01.models import Customer,Apps,DeviceAppUpdate
from rest_framework.response import Response

from rest_framework import viewsets
from app01.serilizer import DeviceAppUpdateSerializers
						



def index(request):
	return HttpResponse('index...')


class DeviceAppUpdateModelView(viewsets.ModelViewSet):
    queryset = DeviceAppUpdate.objects.all()
    serializer_class = DeviceAppUpdateSerializers

    




