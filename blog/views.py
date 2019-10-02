#_-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from blog.models import Article, Comment
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from .forms import ContactForm
from .forms import ArticleForm
from .forms import NouveauContactForm
from .models import Contact
from django.core.mail import send_mail


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
        request,
        'blog/accueil_blog.html',
        {'derniers_articles': articles,
         'date': datetime.now},
    )

def lire(request, id, slug):
    """ Afficher un article complet """
    # try:
    #     article = Article.objects.get(id=id)
    # except Article.DoesNotExist:
    #     raise Http404
    # article = get_object_or_404(Article, id=id)
    article = get_object_or_404(Article, id=id, slug=slug)
    # tri commentaire avec filte sur article
    comments = Comment.objects.filter(article=article)


    return render(request, 'blog/lire.html', {'article': article, 'comments': comments})

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)
    )

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
            context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

######################### Forms ##############################

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True
        # send_mail(
        #     sujet,
        #     message,
        #     envoyeur,
        #     ['jaime.sastre@lapiscine.pro'],
        #     fail_silently=False,
        # )

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

def article(request):

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'blog/articleForm.html', locals())


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/ajoutContact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

####################### exercices ##########################

# def contact(request):
#     return HttpResponse("Page Contact en travaux ;)")

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())