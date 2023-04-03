from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from men.templatetags.men_tags import menu




def index(request):
    posts = Men.objects.all()
    context={
        'posts':posts,
        'title':'Главная страница',
        'cat_selected':0,
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

def show_post(request, post_slug):
    post = get_object_or_404(Men, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'men/post.html', context=context)

def show_category(request, cat_id):
    posts = Men.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'men/index.html', context=context)

def pageNotFound(reuest, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')