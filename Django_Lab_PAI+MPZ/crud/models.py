from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=220)
    number_of_words = models.IntegerField()
    rate = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_edit', kwargs={'pk': self.pk})
