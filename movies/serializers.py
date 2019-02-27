from rest_framework import serializers
from .models import MovieTitles


class MovieTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTitles
        fields = ("title", "director")