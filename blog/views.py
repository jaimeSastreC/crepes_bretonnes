#_-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from blog.models import Article, Categorie
from django.shortcuts import render, get_object_or_404


# Create your views here.


# def index(request):
#     text = """
#     <div style="text-align:center; margin: 3em auto">
#         <h1>Bienvenue sur mon premier<br> <i>Site Django! </i></h1>
#         <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>
#     </div>
#     """
#     return HttpResponse(text)

def index(request):
    """
    page Index avec utilisation de Template et de base en extends
    :param request:
    :return:
    """
    return render(request, 'blog/index.html', {'date': datetime.now})



# def indexBlog(request):
#     text = """
#     <div style="text-align:center; margin: 3em auto">
#         <h1>Bienvenue sur mon premier<br> Blog Django! </h1>
#         <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>
#     </div>
#     """
#     return HttpResponse(text)

def indexBlog(request):
    """
        Afficher tous les articles de notre blog
    """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(
        request, 'blog/accueil_blog.html',
        {'derniers_articles': articles, 'date': datetime.now},
    )

def lire(request, id):
    """ Afficher un article complet """
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'article': article})










def contact(request):
    return HttpResponse("Page Contact en travaux ;)")

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())