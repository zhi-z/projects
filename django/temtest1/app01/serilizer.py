from rest_framework import serializers

from app01.models import Customer,Apps,DeviceAppUpdate



class DeviceAppUpdateSerializers(serializers.ModelSerializer):

      class Meta:
          model=DeviceAppUpdate
          fields="__all__"
          # depth=1

 