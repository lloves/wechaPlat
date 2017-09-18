#from django.conf.urls import url

from . import views
from django.conf.urls import patterns, include, url
from werobot.contrib.django import make_view
from .robot import robot

from werobot import WeRoBot

robot1 = WeRoBot(token='kuaishoudownloadswwww')
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gzh_access/$', views.gzh_access, name='gzh_access'),
    url(r'^robot/', make_view(robot)),
]
