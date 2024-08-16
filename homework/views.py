from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from tzlocal import get_localzone
from os import listdir
from django.urls import reverse

import hw_1.urls


def home_view(request):
    links = "<br>".join(list(map(lambda x: reverse(x.name), hw_1.urls.urlpatterns[1:])))
    return HttpResponse(links)


def current_time(request):
    time_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S") + f" {get_localzone()}"
    return HttpResponse(time_now)


def work_dir(request):
    files = listdir('.')
    prepared_dir = "<br>".join(files)
    return HttpResponse(prepared_dir)
