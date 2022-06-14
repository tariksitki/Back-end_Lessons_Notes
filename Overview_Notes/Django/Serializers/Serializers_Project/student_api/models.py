from django.db import models

# Create your models here.



class Path(models.Model):
    path_name = models.CharField(max_length=10)

    def __str__(self):
        return self.path_name





## Note: DRF template inde create yaparken serializer da path olmadigi icin path secimi yapamiyoruz. Bu nedenle burada path kisminda null=True demedigimizde, template den post islemi yapamadik. Null true dedigimizde ise, ögrenci create ettigimizde path  kismi null oluyor.
## Diger bir cözüm olarak da default atamayi kullandik.

## Burada iki tane modelimiz var. Bu modellerden student icinde path yazdik ve bunu foreign key ile bagladik. Bu nedenle, db de student tablomuza baktigimizda; bunun icinde path_id column u görürüz. ama path tablosuna gittigimizde;  burada student ile ilgili birsey görmeyiz.




class Student(models.Model):
    path = models.ForeignKey(Path, related_name="students", on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(null=True)
    register_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.number}, {self.first_name}, {self.last_name}"
    