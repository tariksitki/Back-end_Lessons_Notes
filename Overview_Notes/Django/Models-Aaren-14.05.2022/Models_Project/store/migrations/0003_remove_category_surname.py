# Generated by Django 4.0.4 on 2022-05-15 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='surname',
        ),
    ]