# Generated by Django 3.2 on 2021-05-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShopUser',
        ),
    ]
