from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


def validate_rating(value):
    if value < 0 or value > 10:
        raise ValidationError('Rating must be between 0 and 10.')


def validate_release_year(value):
    if value > date.today().year:
        raise ValidationError(f'Release year cannot be later than {date.today().year}.')


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.IntegerField(validators=[validate_release_year])
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[validate_rating])
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
