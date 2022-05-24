from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    ## burada slugField kullanimi ile hepsi burada gibi url de id görünmez

    class Meta:
        verbose_name_plural = "Ögrenciler"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    ## Note: bizim modelimizin adi Student ama admin panele gittigimizde, Students olarak görüyoruz. Bunu kendisi otomatik olarak yapiyor. 

