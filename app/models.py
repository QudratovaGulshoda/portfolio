import uuid
from django.db import models
from django.utils.html import format_html


# Base model class that provides common fields and functionalities for other models to inherit from
class BaseModel(models.Model):
    # Unique identifier for each instance of the model
    id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, primary_key=True)

    # DateTimeField that automatically stores the creation time of an instance when it is first saved to the database
    created_at = models.DateTimeField(auto_now_add=True)

    # DateTimeField that automatically updates with the current time whenever the instance is saved or updated in the
    # database
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Specifies that this model is abstract, meaning it won't be created as a separate table in the database
        abstract = True


# Create your models here.
class Contact(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=150, unique=True)
    message = models.TextField()

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class News(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="image", null=True, blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def picture(self):
        if self.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(
                    self.image.url
                )
            )
        return "no_image"

    class Meta:
        db_table = "news"
        verbose_name = "News"
        verbose_name_plural = "News"


class ServiceTariff(BaseModel):
    class CategoryChoice(models.IntegerChoices):
        IT_PARK = 1, "IT Park"

        IT_PARK1 = 2, "IT Park"
        IT_PARK2 = 3, "IT Park"
        IT_PARK3 = 4, "IT Park"
        IT_PARK4 = 5, "IT Park"

    class TitleChoices(models.IntegerChoices):
        e = 1, "Бухгалтерский аутсорсинг для резидентов IT Park"
        a = 2, "Бухгалтерский аутсорсинг для производственных предприятий"
        b = 3, "Бухгалтерский аутсорсинг для оптовой торговли"
        c = 4, "Бухгалтерский аутсорсинг для предприятий общепита"
        d = 5, "Бухгалтерский аутсорсинг для предприятий оказывающие услуги"

    class TurnoverChoices(models.IntegerChoices):
        INCLUDE = 1, "Включено"
        NOT_INCLUDED = 2, "Не включено"

    name = models.CharField(max_length=500)

    category = models.IntegerField(choices=CategoryChoice.choices)
    title = models.IntegerField(choices=TitleChoices.choices)

    field1 = models.IntegerField(choices=TurnoverChoices.choices)
    field2 = models.IntegerField(choices=TurnoverChoices.choices)
    field3 = models.IntegerField(choices=TurnoverChoices.choices)
    field4 = models.IntegerField(choices=TurnoverChoices.choices)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "serviceTariff"
        verbose_name = "ServiceTariff"
        verbose_name_plural = "ServiceTariffs"


