from django.contrib import admin

from app.models import News, Contact, ServiceTariff


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceTariff)
class ServiceTariffAdmin(admin.ModelAdmin):
    pass
