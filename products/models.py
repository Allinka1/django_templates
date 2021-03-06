from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=False, blank=True)

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categoryies'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def __repr__(self):
        return f'<Category ("{self.cid}")>'

    def __str__(self):
        return self.category


class Products(models.Model):
    pid = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'<Products ("{self.pid}")>'
