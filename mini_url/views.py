from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MiniUrl
from .forms import MiniUrlForm

# Create your views here.

def apps(request):
    text = """
    <div style="text-align:center; margin: 3em auto">
        <h1>Bienvenue sur mon app<br></h1>
        <p>test de page et app</p>
    </div>
    """
    return HttpResponse(text)

def liste(request):
    """ Affichage des redirections"""
    minis = MiniUrl.objects.order_by('-nb_acces')

    return render(request, 'mini_url/liste.html', locals())

def nouveau(request):
    """Ajouter une redirection"""
    if request.method == "POST":
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
            form = MiniUrlForm

    return  render(request, 'mini_url/nouveau.html', {'form': form})

def redirection(request, code):
    """Redirection vers l'URL enregistré"""
    mini = get_object_or_404(MiniUrl, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent= True)