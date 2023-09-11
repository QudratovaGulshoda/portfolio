from rest_framework import serializers
from app.models import News, Contact, ServiceTariff


# Define a serializer for the Contact model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact  # Specify the model to be serialized (Contact)
        fields = ["id", "name", "message"]  # Specify the fields to include in the serialization


# Define a serializer for the News model
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News  # Specify the model to be serialized (News)
        fields = ["id", "title", "description", "created_at",
                  "image"]  # Specify the fields to include in the serialization


# Define a serializer for the ServiceTariff model
class ServiceTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTariff  # Specify the model to be serialized (ServiceTariff)
        fields = ["id", "name"]  # Specify the fields to include in the serialization

    def to_representation(self, instance):
        rep = super().to_representation(instance=instance)  # Call the parent class's to_representation method

        # Add additional fields to the serialized representation
        rep["title"] = instance.get_title_display()
        rep["category"] = instance.get_category_display()

        rep["field1"] = instance.get_field1_display()
        rep["field2"] = instance.get_field2_display()
        rep["field3"] = instance.get_field3_display()
        rep["field4"] = instance.get_field4_display()

        rep["asliddin"] = "asliddin"  # Add a custom field "asliddin" with a fixed value

        return rep  # Return the modified serialized representation
