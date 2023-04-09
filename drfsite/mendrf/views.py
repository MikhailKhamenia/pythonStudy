
from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *


# Create your views here.
class MenAPIView(generics.ListAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer