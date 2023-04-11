from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer

class MenAPIView(APIView):
    def get(self, request):
        m = Men.objects.all()
        return Response({'posts': MenSerializer(m,many=True).data})

    def post(self, request):
        serializer = MenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT is not allowed'})

        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({'error':'Object does not exist'})

        serializer = MenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE is not allowed'})

        try:
            instance = Men.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exist'})
        return Response({'post': 'delete_post'+str(pk)})

# Create your views here.
#class MenAPIView(generics.ListAPIView):
#    queryset = Men.objects.all()
#    serializer_class = MenSerializer