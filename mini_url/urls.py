from django.conf.urls import url
from . import views

#distinguer par nespace de nom
app_name = 'mini_url'

urlpatterns = [
    url(r'apps/', views.apps, name='apps')
]