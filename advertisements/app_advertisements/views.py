from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Успшно! Это главная страница')


def page1(request):
    return HttpResponse('Успшно! Это обычная страница')