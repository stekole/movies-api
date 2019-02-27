from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import MovieTitles
from .serializers import MovieTitlesSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_movie(title="", director=""):
        if title != "" and director != "":
            MovieTitles.objects.create(title=title, director=director)

    def setUp(self):
        # add test data
        self.create_movie("godfather", "francis ford coppola")
        self.create_movie("forgetting sarah marshall", "Nicholas Stoller")
        self.create_movie("goodfellas", "martin scorsese")


class GetAllMovieTitlesTest(BaseViewTest):

    def test_get_all_MovieTitles(self):
        """
        This test ensures that all MovieTitles added in the setUp method
        exist when we make a GET request to the MovieTitles/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("movies-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = MovieTitles.objects.all()
        serialized = MovieTitlesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


