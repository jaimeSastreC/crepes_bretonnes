from django.conf.urls import url
from . import views

#distinguer par nespace de nom
app_name = 'mini_url'

urlpatterns = [
    url(r'^$', views.liste, name='url_liste'),
    url(r'apps', views.apps, name='url_apps'),
    url(r'list.html', views.liste, name='url_liste'),
    url(r'nouveau.html', views.nouveau, name='url_nouveau'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection')
]


