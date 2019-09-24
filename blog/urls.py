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
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
# ajouté accueil => home
from . import views

urlpatterns = [
    path('index/', views.indexBlog, name='index'),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('contact/', views.contact, name='contact'),
    #path('article/<int:id>', views.lire, name='lire')
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
]


handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'