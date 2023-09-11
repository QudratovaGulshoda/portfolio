from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from app.models import News, Contact
from app.serializers import Newsserializer, Contactserializer
from rest_framework.filters import SearchFilter


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Contactserializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = Newsserializer
