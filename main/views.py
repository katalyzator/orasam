from django.shortcuts import render


def index_view(request):
    context = {}
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
