from django.shortcuts import render
from rest_framework import viewsets
from .serializer import RestaurantSerializer  # Adjust the import based on your project structure
from .models import Restaurant  # Adjust the import based on your project structure

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()