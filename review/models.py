from django.db import models
from django.utils import timezone
from datetime import timedelta
from products.models import Products



class Review(models.Model):

    RATE_CHOICES = [
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]
    ]

    rid = models.AutoField(primary_key=True)
    body = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=False)
    rating = models.IntegerField(choices=RATE_CHOICES, default=5)
    created_at = models.DateTimeField()

    def save(self, **kwargs):
        if not self.rid:
            self.created_at = timezone.now() - timedelta(days=365)
        super().save(**kwargs)

    def __str__(self):
        return f'{self.product} {self.body} {self.created_at}'
