from django.db import models
from django.utils.html import format_html


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, unique=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class News(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="image", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
        db_table = ""
        managed = True
        verbose_name = "News"
        verbose_name_plural = "News"
