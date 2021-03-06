# Generated by Django 3.2 on 2021-05-16 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Product category', 'verbose_name_plural': 'Product categoryies'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category'),
        ),
    ]
