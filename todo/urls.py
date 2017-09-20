# coding:utf-8
from django.conf.urls import include, url
from views import todo_event

urlpatterns = [
    url(r'$', todo_event),
    ]