from django.shortcuts import render

from django.http import response


def index(request):
    return response.HttpResponse('This is index of news')

def test(request):
    return response.HttpResponse('This is test of newS')