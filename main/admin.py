# coding=utf-8
from django.contrib import admin

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


class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book


class SliderImageAdmin(admin.ModelAdmin):
    class Meta:
        model = SliderImage


class PartnersAdmin(admin.ModelAdmin):
    class Meta:
        model = Partner


admin.site.register(Partner, PartnersAdmin)

admin.site.register(SliderImage, SliderImageAdmin)

admin.site.register(Book, BookAdmin)

admin.site.register(NewsImage, NewsImageAdmin)

admin.site.register(EventImage, EventImageAdmin)

admin.site.register(PublicationImage, PublicationImageAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(Publications, PublicationAdmin)
