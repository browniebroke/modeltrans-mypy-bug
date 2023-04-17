from django.db import models
from modeltrans.fields import TranslationField


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    i18n = TranslationField(fields=("name",))

    def __str__(self):
        return self.name