from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ContactViewSet, NewsViewSet

router = DefaultRouter()
router.register("contact", ContactViewSet)
router.register("news", NewsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
