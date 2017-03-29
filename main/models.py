# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode

from main.helper import transform

pathNews = 'news/images'
pathEvent = 'events/images'
TYPE_NEWS = (('uluslar', 'Uluslar arasi iliskiler'),
             ('ekonomi', 'ekonomi'),
             ('enerji', 'enerji'),
             ('siyaset', 'siyaset'),
             ('toplum', 'toplum'),
             )


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление новостей'
        verbose_name = 'Добавление новостей'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')
    news_type = models.CharField(choices=TYPE_NEWS, verbose_name='Тип новости', max_length=100)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Event(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление мероприятий'
        verbose_name = 'Добавление мероприятий'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class NewsImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки новостей'
        verbose_name = 'Картинки новостей'

    news = models.ForeignKey(News, verbose_name='выберите новость')
    image = models.ImageField(upload_to=transform(pathNews), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.news.title)


class EventImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки мероприятий'
        verbose_name = 'Картинки мероприятий'

    event = models.ForeignKey(Event, verbose_name='выберите мероприятие')
    image = models.ImageField(upload_to=transform(pathEvent), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.event.title)


class Publications(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление публикаций'
        verbose_name = 'Добавление публикаций'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class PublicationImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки публикаций'
        verbose_name = 'Картинки публикаций'

    publication = models.ForeignKey(Publications, verbose_name='выберите публикацию')
    image = models.ImageField(upload_to=transform(pathEvent), verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.publication.title)
