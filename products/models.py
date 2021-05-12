from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=False, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


class Products(models.Model):
    pid = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
