# Generated by Django 4.0.5 on 2022-06-14 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.IntegerField(null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('path', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student_api.path')),
            ],
        ),
    ]
