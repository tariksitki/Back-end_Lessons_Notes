# Generated by Django 4.0.4 on 2022-05-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0007_student_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]
