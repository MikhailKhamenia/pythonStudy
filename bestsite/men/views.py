from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu=['О сайте', 'Добавить статью','Обратная связь','Войти']

def index(request):
    posts = Men.objects.all()
    return render(request, 'men/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'men/about.html', {'menu': menu,'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1> Categories of article </h1><p>{catid}</p>')

def archive(request, year):
    #if int(year)>=2024:
        #raise Http404()
    if int(year)>2023:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Archive of years</h1><p>{year}</p>')

def pageNotFound(reuest, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')