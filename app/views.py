from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions, response, status

from app.models import News, Contact, ServiceTariff
from app.serializers import NewsSerializer, ContactSerializer, ServiceTariffSerializer


from rest_framework import status
from rest_framework.response import Response

from rest_framework import generics, status
from rest_framework.response import Response


from rest_framework import generics, permissions


class ContactViewSet(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]



# Define a view for listing news items (GET request)
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()  # Retrieve all news items from the database
    serializer_class = NewsSerializer  # Use the NewsSerializer to serialize the data
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view


# Define a view for retrieving a single news item by ID (GET request)
class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()  # Retrieve all news items from the database
    serializer_class = NewsSerializer  # Use the NewsSerializer to serialize the data
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view
    lookup_url_kwarg = "news_id"  # Define the URL keyword argument for the news item ID


# Define a custom view for serving service tariff data (GET request)
class ServiceTariffViews(generics.GenericAPIView):
    serializer_class = ServiceTariffSerializer  # Use the ServiceTariffSerializer to serialize the data
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view

    def get_object(self):
        obj = ServiceTariff.objects.all()  # Retrieve all service tariff objects from the database
        return obj

    def get(self, request):
        queryset = self.get_object()  # Get the service tariff queryset
        serialized_data = self.serializer_class(queryset, many=True)  # Serialize the queryset

        return response.Response(
            data={
                "success": True,
                "err_code": 0,
                "err_msg": "",
                "data": serialized_data.data  # Include serialized data in the response
            },
            status=status.HTTP_200_OK  # Set the HTTP status code to 200 (OK)
        )
