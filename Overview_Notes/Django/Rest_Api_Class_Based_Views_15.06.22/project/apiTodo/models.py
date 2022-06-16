from django.db import models

# Create your models here.



class Todo(models.Model):
    CHOICES = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low")
    )
    task = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=CHOICES, default="L")
    done = models.BooleanField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task


## Note: priority de default deger girerken;  human redable olan kismi degil db nin görecegi kismi yazacagiz. Yani  L yazdik.