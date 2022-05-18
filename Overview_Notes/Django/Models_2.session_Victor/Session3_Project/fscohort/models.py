
from email.policy import default
from django.db import models

# Create your models here.


class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", 'Freshman'),
        ("SP", 'Sophomore'),
        ("JR", 'Junior'),
        ("SR", 'Senior'),
        ("GRD", 'Graduate'),
    ]
    ## Buradaki veriler tuple formatinda. Admin panel de choices yaparken, Buradaki tuple in ikinci elemanlar karsimiza cikarilir.  Ama biz secim yaptiktan sonra, db ye ilk eleman olan kisa halleri yazilir.

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    about = models.TextField(null = True, blank=True)
    avatar = models.ImageField(null = True, blank = True, upload_to = "media/", default = "media/IMG_0499.JPG/")
    register_date = models.DateTimeField(auto_now_add=True)
    # datetimefield da saat de gelir. Sadece dateNow da ise tarih gelir.
    # ve burada sadece kayit tarihleri  alinir ve o tarih sabit kalir.

    update_date = models.DateTimeField(auto_now=True)
    # sadece auto_now oldugunda ise; kullanici her degisiklik yaptiginda tarih update edilir.

    year_in_school = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, default= "FR")
    ## CharField da max-length girmek zorundayiz. O nedenle ve choice da db ye kaydedilecek verilerimiz en cok 3 karakter oldugundan 3 yazdik.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ögrenciler"
        # db_table = "Student_Table"
        # Bu tablo db de tablo adi degistirir.
