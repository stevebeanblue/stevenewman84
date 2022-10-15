import datetime

from django.db import models
from tinymce import models as tinymce_models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField()
    date = datetime.date

    def __str__(self):
        return self.title


class WorkingWith(models.Model):
    name = models.CharField(max_length=100)
    description = tinymce_models.HTMLField()
    image_link = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.name
