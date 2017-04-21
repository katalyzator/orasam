from django.http import Http404
from django.shortcuts import render
from .models import *


def index_view(request):
    sliderimage = SliderImage.objects.all()
    news = News.objects.all()
    event = Event.objects.all()
    publication = Publications.objects.all()
    context = {"news": news, "events": event, "publication": publication, "slides": sliderimage}
    template = 'main/main_page.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about.html'

    return render(request, template, context)


def acitivity_view(request):
    event = Event.objects.all()
    context = {"events": event}
    template = 'activities.html'

    return render(request, template, context)


def all_news_view(request):
    news = News.objects.all()
    context = {"news": news}
    template = 'all_news.html'

    return render(request, template, context)


def book_view(request):
    book = Book.objects.all()
    context = {"books": book}
    template = 'books.html'

    return render(request, template, context)


def contacts_view(request):
    context = {}
    template = 'contacts.html'

    return render(request, template, context)


def country_view(request):
    news = News.objects.all()

    context = {"news": news}
    template = 'countries.html'

    return render(request, template, context)


def group_view(request):
    context = {}
    template = 'groups.html'

    return render(request, template, context)


def member_view(request):
    members = Employee.objects.all()
    context = {"members": members}
    template = 'members.html'

    return render(request, template, context)


def partners_view(request):
    partners = Partner.objects.all()
    context = {"partners": partners}
    template = 'partners.html'

    return render(request, template, context)


def projects_view(request):
    context = {}
    template = 'projects.html'

    return render(request, template, context)


def bulten_view(request):
    context = {}
    template = 'bultenler.html'

    return render(request, template, context)


def degerlendirme_view(request):
    context = {}
    template = 'degerlendirmeler.html'

    return render(request, template, context)


def raporlar_view(request):
    context = {}
    template = 'raporlar.html'

    return render(request, template, context)


def makale_country_view(request):
    news = News.objects.all()
    context = {"news": news}
    template = 'm_countries.html'

    return render(request, template, context)


def makale_konu_view(request):
    news = News.objects.all()
    context = {"news": news}
    template = 'm_news.html'

    return render(request, template, context)


def single_news(request, id):
    try:
        news = News.objects.get(id=id)

        context = {"news": news}
        template = 'single_post.html'
        print news.title

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404


def single_publication(request, id):
    try:
        publications = Publications.objects.get(id=id)

        context = {"publications": publications}
        template = 'single_publication.html'

        return render(request, template, context)

    except Publications.DoesNotExist:
        raise Http404


def single_event(request, id):
    try:
        events = Event.objects.get(id=id)

        context = {"events": events}
        template = 'single_event.html'

        return render(request, template, context)

    except Event.DoesNotExist:
        raise Http404
