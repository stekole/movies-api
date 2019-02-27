from django.db import models


class MovieTitles(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of director 
    director = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.director)