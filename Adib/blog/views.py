from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class ListHouseInfoView(generics.ListAPIView):
    queryset = HouseInfo.objects.all()
    serializer_class = HouseInfoSerializer


class DetailHouseInfoView(generics.RetrieveAPIView):
    queryset = HouseInfo.objects.all()
    serializer_class = HouseInfoSerializer


class CreateContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer





