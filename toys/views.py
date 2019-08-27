from django.shortcuts import render

from rest_framework import viewsets

from .models import Toy, Brand, Category
from .serializers import ToySerializer, BrandSerializer, CategorySerializer
# Create your views here.

class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
