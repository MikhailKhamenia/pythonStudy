from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu=[{'title':'О сайте','url_name':'about'},
      {'title':'Добавить статью','url_name':'add_page'},
      {'title':'Обратная связь', 'url_name':'contact'},
      {'title':'Войти','url_name':'login'}
      ]

def index(request):
    posts = Men.objects.all()
    context={
        'posts':posts,
        'menu': menu,
        'title':'Главная страница'
    }
    return render(request, 'men/index.html', context=context)

def about(request):
    return render(request, 'men/about.html', {'menu': menu,'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Добалвение статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id= {post_id}')

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