from django.urls import path
from app import views


# Define URL patterns for your Django application
urlpatterns = [
    # URL pattern for retrieving a single news item by ID
    # The '<str:news_id>' part captures a string parameter 'news_id' from the URL
    # It maps to the 'news_id' parameter in your view
    path("news/<str:news_id>", views.NewsDetailView.as_view()),

    # URL pattern for listing news items
    # This pattern maps to the NewsListView class view
    path("news", views.NewsListView.as_view()),
    path("contact", views.ContactViewSet.as_view()),
    # URL pattern for serving service tariff data
    # This pattern maps to the ServiceTariffViews class view
    path("service-tariff", views.ServiceTariffViews.as_view()),
]
