from django.db import models

# Create your models here.


class Creator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # one to one


class Language(models.Model):
    name = models.CharField(max_length=30)
    yazari = models.OneToOneField(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

        # many to one (mesela bir kisinin birden cok blog u olabilir. mesel aben hem hayvanlar hakkinda hem de  it alaninda blog yazmis olabilirm. ama bir blog sadece bir kisiye ait olabilir. benim blogum baskasina ait olamaz.)


# class Frameworks(models.Model):
#     name = models.CharField(max_length=20)
#     language = models.ForeignKey(Language, on_delete=models.SET_NULL, null = True)

#     def __str__(self):
#         return self.name

class Frameworks(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default = 19)

    def __str__(self):
        return self.name

        # many to many iliski:
        # Elimizde bir kisiler tablosu olsun birde frameworkler.  Bir kisi birden cok framework bilebilir. Ve bir framework de birden cok kisi tarafindan bilinebilir.

        # Ancak bir satbloda bunu göstermek olanaksizdir. Cünkü bir kisinin bildigi framework karsisina sadece bir tane framework un id si yazilabilir.

        # Bu nedenle biz bu tür bir iliski olusturdugumuzda, django otomatik olarak yeni bir tablo olusturur.

        # Birde bu iliskide bir framework bircok kisi tarafindan bilindigi icin, verilerden biri silindiginde digeri ne olsun diye sorulmaz. Cünkü baska kisiler tarafindan bilinmeye devam edecektir.

        # admin panel de developers olustururken,  bir kisinin bildigi frameworkler secilirken ctrl tusuna basili tutarak birden cok framework secilebilir.


class Developers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    frameworks = models.ManyToManyField(Frameworks)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# CASCADE : Verilerden biri silinirse digerini de sil

# SET_NULL : verilerden biri silindiginde diger tabloda null atar. Bunun icin yazari kisminda null = True dememiz gerekir.

# SET_DEFAULT : silindiginde bizim atadigimiz default degeri atar. Bunun icin language tablomuzda yazari kismina default deger atamamiz gerekir.

# DO_NOTHING : Hicbir sey yapma

# PROTECT : eger bagli oldugu bir parent iliskisi var ise digerini silmemize izin vermez
