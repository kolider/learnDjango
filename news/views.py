from django.shortcuts import render

from .models import News

from django.http import response


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

def test(request):
    return response.HttpResponse('This is test of newS')