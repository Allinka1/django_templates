from django.db import models
from products.models import Products


# Create your models here.


class Review(models.Model):
    rid = models.AutoField(primary_key=True)
    body = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=False)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.body
