from django.contrib import admin

# Register your models here.
from main.models import *


class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = News


class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event


class PublicationAdmin(admin.ModelAdmin):
    class Meta:
        model = Publications


class NewsImageAdmin(admin.ModelAdmin):
    class Meta:
        model = NewsImage


class EventImageAdmin(admin.ModelAdmin):
    class Meta:
        model = EventImage


class PublicationImageAdmin(admin.ModelAdmin):
    class Meta:
        model = PublicationImage


admin.site.register(NewsImage, NewsImageAdmin)

admin.site.register(EventImage, EventImageAdmin)

admin.site.register(PublicationImage, PublicationImageAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(Publications, PublicationAdmin)
