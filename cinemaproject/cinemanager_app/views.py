from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics
# Create your views here.



class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer