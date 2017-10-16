from django.db import models
from django.db.models import CharField, IntegerField, TextField
from django_extensions.db.models import TimeStampedModel


class Crop(TimeStampedModel):
    name = CharField(max_length=128)
    description = TextField(blank=True)
    spacing = IntegerField(default=-1)
    # spacing_unit = models.


class CropVariety(TimeStampedModel):
    name = CharField(max_length=128)
    description = TextField(blank=True)
