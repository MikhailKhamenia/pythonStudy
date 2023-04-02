from django.urls import path, re_path

from men.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categories/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)

]