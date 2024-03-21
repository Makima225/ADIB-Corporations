from rest_framework import serializers
from .models import HouseInfo, Contact


class HouseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseInfo
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
