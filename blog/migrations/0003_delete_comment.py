# Generated by Django 3.2 on 2021-04-24 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210424_2254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
