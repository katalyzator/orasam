# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode

from main.helper import transform

pathNews = 'news/images'
pathEvent = 'events/images'
TYPE_NEWS = (
    ('uluslar', 'Uluslar arasi iliskiler'),
    ('ekonomi', 'ekonomi'),
    ('enerji', 'enerji'),
    ('siyaset', 'siyaset'),
    ('toplum', 'toplum'),
    ('tarim', 'TARIM'),
    ('hukuk', 'hukuk'),
    ('iletisim', 'Iletisim'),
    ('Guvenlik', 'Guvenlik'),
)

COUNTRIES = (
    ('Afganistan', 'Afganistan'),
    ('Azerbaycan', 'Azerbaycan'),
    ('China', 'China'),
    ('Hindistan', 'Hindistan'),
    ('Kazakistan', 'Kazakistan'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Russia', 'Russia'),
    ('Tajikistan', 'Tajikistan'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
)


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление новостей'
        verbose_name = 'Добавление новостей'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')
    image = models.ImageField(upload_to=transform(pathNews), verbose_name='картинка')
    news_type = models.CharField(choices=TYPE_NEWS, verbose_name='Тип новости', max_length=100)
    country = models.CharField(max_length=255, choices=COUNTRIES, verbose_name='Страна')

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
    image = models.ImageField(upload_to=transform(pathEvent), verbose_name='картинка')

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
    image = models.ImageField(upload_to=transform(pathEvent), verbose_name='картинка')

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


class Book(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление книг'
        verbose_name = 'Добавление книг'

    title = models.CharField(max_length=255, verbose_name='Название книги')
    editor = models.CharField(max_length=255, verbose_name='главный редактор')
    redaktor = models.CharField(max_length=255, verbose_name='редактор')
    prepare = models.CharField(max_length=255, verbose_name='подготовили')
    description = models.CharField(max_length=255, verbose_name='описание')
    image = models.ImageField(upload_to=transform('images/books'), verbose_name='картинка книги')
    link_download = models.URLField(verbose_name='ссылка для скачивания')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class SliderImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки слайдера'
        verbose_name = 'картинки слайдера'

    image = models.ImageField(upload_to=transform('images/sliderimage'), verbose_name='картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.id)


class Partner(models.Model):
    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнеры'

    title = models.CharField(max_length=255, verbose_name='Название организации')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(upload_to=transform('images/partners'), verbose_name='Фотографии(логотип)')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Employee(models.Model):
    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудники'

    name = models.CharField(max_length=255, verbose_name='ФИО сотрудника')
    position = models.CharField(max_length=255, verbose_name='должность')
    description = models.CharField(max_length=255, verbose_name='описание должности')

    image = models.ImageField(upload_to=transform('images/employee'), verbose_name='Фотография сотрудника')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)
