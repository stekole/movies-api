
from rest_framework import generics
from .models import MovieTitles
from .serializers import MovieTitlesSerializer


class ListMovieView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = MovieTitles.objects.all()
    serializer_class = MovieTitlesSerializer

