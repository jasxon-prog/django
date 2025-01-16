from django.db import models
from user.models import User


# Movie db
class Genre(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class MovieTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


UZ, RU, EN = "uz", "ru", "en"


class Movie(models.Model):
    class LanguageChoices(models.TextChoices):
        UZ = (UZ, "Uzbek")
        RU = (RU, "Russian")
        EN = (EN, "English")

    language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, default=UZ
    )
    title = models.CharField(max_length=200, unique=True)
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    age_limit = models.IntegerField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    movie_year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="movies/", null=True, blank=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} liked {self.movie.title}"
