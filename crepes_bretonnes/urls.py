"""crepes_bretonnes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    oui!!!
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
#pour visualiser images
from django.conf import settings
from django.conf.urls.static import static

# ajouté accueil => home
from blog import views
# from mini_url import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('mini_url/', include('mini_url.urls')),
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]

# debug
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

# pour visualiser images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)