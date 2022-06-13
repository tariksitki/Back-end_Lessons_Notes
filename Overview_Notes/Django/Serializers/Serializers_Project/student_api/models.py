from django.db import models

# Create your models here.



class Path(models.Model):
    path_name = models.CharField(max_length=10)

    def __str__(self):
        return self.path_name





## Note: burada path kisminda null=True demedigimizde, template den post islemi yapamadik. Null true dedigimizde ise, ögrenci create ettigimizde path  kismi null oluyor.
class Student(models.Model):
    path = models.ForeignKey(Path, related_name="students", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(null=True)
    register_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.last_name