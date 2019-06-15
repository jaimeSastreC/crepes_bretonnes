#_-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    text = """ 
    <div style="text-align:center; margin: 3em auto">
        <h1>Bienvenue sur mon premier<br> <i>Site Django! </i></h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>
    </div>
    """
    return HttpResponse(text)



def indexBlog(request):
    text = """ 
    <div style="text-align:center; margin: 3em auto">
        <h1>Bienvenue sur mon premier<br> Blog Django! </h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>
    </div>
    """
    return HttpResponse(text)
