from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from men.templatetags.men_tags import menu

class MenHome(ListView):
    template_name = 'men/index.html'
    context_object_name = 'posts'
    model=Men
    extra_context = {'title': "Главная страница"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cat_selected']=0
        return context

    def get_queryset(self):
        return Men.objects.filter(is_published=True)
#def index(request):
#    posts = Men.objects.all()
#    context={
#        'posts':posts,
#        'title':'Главная страница',
#        'cat_selected':0,
#    }
#    return render(request, 'men/index.html', context=context)

def about(request):
    return render(request, 'men/about.html', {'menu': menu,'title': 'О сайте'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'men/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Добавления статьи'
        return context

#def addpage(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#             print(form.cleaned_data)
#                #Men.objects.create(**form.cleaned_data)
#            form.save()
#            return redirect('home')
#    else:
#       form = AddPostForm()
#    return render(request, 'men/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

class ShowPost(DetailView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=context['post']
        return context

#def show_post(request, post_slug):
#    post = get_object_or_404(Men, slug=post_slug)
#
#    context = {
#        'post': post,
#        'title': post.title,
#        'cat_selected': post.cat_id,
#    }
#
#    return render(request, 'men/post.html', context=context)

class MenCategory(ListView):
    template_name = 'men/index.html'
    context_object_name = 'posts'
    model=Men
    allow_empty = False

    def get_queryset(self):
        return Men.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cat_selected']=context['posts'][0].cat_id
        return context

#def show_category(request, cat_id):
#    posts = Men.objects.filter(cat_id=cat_id)
#
#    if len(posts) == 0:
#        raise Http404()
#
#    context = {
 #       'posts': posts,
 #       'title': 'Отображение по рубрикам',
 #       'cat_selected': cat_id,
 #   }
 #   return render(request, 'men/index.html', context=context)

def pageNotFound(reuest, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')