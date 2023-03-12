from django.core.exceptions import ValidationError
from django.db import models


def validate_ingredients(value):
    if ', ' not in value:
        raise ValidationError('The ingredients must be separated by ", ".')


class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
    )

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250,
        validators=(
            validate_ingredients,
        ),
    )

    time = models.IntegerField(
        verbose_name='Time(Minutes)'
    )

    class Meta:
        ordering = ('id', )


