from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ögrenciler"
        # db_table = "Student_Table"
        # Bu tablo db de tablo adi degistirir.
