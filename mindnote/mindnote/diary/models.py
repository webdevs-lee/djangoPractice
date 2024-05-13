from django.db import models
from .validators import *
from datetime import date

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, validators=[validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=80, validators=[validate_no_numbers])
    score = models.IntegerField(validators=[validate_score])
    date = models.DateField(verbose_name="Date Real", default=date.today(), validators=[validate_date])
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)

    def __str__(self):
        return self.title
    