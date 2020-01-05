from datetime import date

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

def upload_file(instance, filename):
    return f"Ara_Ara/anime/{date.today()}_{filename}"


class Anime(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=100, null=True, blank=True)
    synopsis = models.TextField(blank=True, default="")
    poster = models.ImageField(upload_to=upload_file, blank=True, default="Ara_Ara/logo.png")
    status = models.CharField(max_length=1,
                              choices=(('a', "Airing"), ('n', "Not Yet Aired"), ('f', "Finished Airing")), default='n')
    duration = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    season = models.CharField(max_length=2,
                              choices=(('sp', "Spring"), ('sm', "Summer"), ('fa', "Fall"), ('wn', "Winter")), null=True,
                              blank=True)
    total_eps = models.IntegerField(default=12, null=True, blank=True)
    aired_eps = models.IntegerField(default=0)
    rating = models.CharField(max_length=4,
                              choices=(
                                  ('g', "General Audiences"),
                                  ('pg', "Parental Guidance"),
                                  ('pg13', "Teens - 13 or above"),
                                  ('r', "Some Mature Content"),
                                  ('nc17', "Mature - 17 or above"),
                                  ('nr', "No Rating"),
                              ), default='nr')

    def __str__(self):
        return f"Anime ID {self.id} : {self.name}"

    class Meta:
        db_table = 'Anime'


class Review(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(default="")
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)

    def __str__(self):
        return f"Review ID {self.id} : {self.anime.name} by {self.user.username}"

    class Meta:
        db_table = 'Review'
