from django.shortcuts import render
from .models import *


def index_view(request):
    news = News.objects.all()
    event = Event.objects.all()
    publication = Publications.objects.all()
    context = {"news": news, "events": event, "publication": publication}
    template = 'main/main_page.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about.html'

    return render(request, template, context)


def acitivity_view(request):
    context = {}
    template = 'activities.html'

    return render(request, template, context)


def all_news_view(request):
    context = {}
    template = 'all_news.html'

    return render(request, template, context)


def book_view(request):
    context = {}
    template = 'books.html'

    return render(request, template, context)


def contacts_view(request):
    context = {}
    template = 'contacts.html'

    return render(request, template, context)


def country_view(request):
    context = {}
    template = 'countries.html'

    return render(request, template, context)


def group_view(request):
    context = {}
    template = 'groups.html'

    return render(request, template, context)


def member_view(request):
    context = {}
    template = 'members.html'

    return render(request, template, context)


def partners_view(request):
    context = {}
    template = 'partners.html'

    return render(request, template, context)


def projects_view(request):
    context = {}
    template = 'projects.html'

    return render(request, template, context)
