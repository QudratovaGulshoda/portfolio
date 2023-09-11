from rest_framework import serializers
from app.models import News, Contact


class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "name", "message", "created_at")


class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "description", "created_at", "image")
