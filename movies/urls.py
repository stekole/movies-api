from django.urls import path
from .views import ListMovieView


urlpatterns = [
    path('movietitles/', ListMovieView.as_view(), name="movies-all")
]