

from rest_framework import serializers
from .models import Student, Path
from django.db import models
from django.utils.timezone import now

## Note: serializer kisminda, model de olusturdugumuz class a ait field lari gösterebiliriz. Eger model de olmayan bir field i seria da göstermek istersek hata aliriz.

## Note: burada yazdigimiz validation lar admin paneldeki girislerimizi etkilemez. sadece rest framework icin gecerlidir.

# burada StudentSerializer altinda belirledigimiz isimler bizim dönüstürmek istedigimiz verilerdir. Bu veriler json a dönüsecek. Bunu serializers yapacak.
# Ayrica bunlarin view da öncelikle islemleri yapilacak, daha sonra url.py da kullanicinin son görecegi hale gelecek.

## Bu ilk yöntem. Burada herseyi manuel kendimiz yaptik.
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     last_name = serializers.CharField(max_length=200)
#     number = serializers.IntegerField()

    # Not: Normalde models.py da 5 tane field var. ama biz burada 3 tanesini json a dönüstürdügümüz icin, kullanici 3 tane field görüyordu. Bir buna ilave olarak birde id görsün istiyoruz. Models de id yok ama django kendisi db de otomatik olusturur. simdi biz bu hazir id yi user a sunuyoruz.
    # id = serializers.IntegerField()

    # su ana kadar yazdigimiz kodlar ile sadece json formatinda okuma islemi yapabiliriz. Eger template de post islemi yapmak istersek hata aliriz. Bu nedenle simdi asagidaki kodlari yazacagiz:

    # def create(self, validated_data):
    #         return Student.objects.create(**validated_data)
    #     ## eger user tarafindan girilen veri validated ise, bu bilgiler ile yeni bir veri create ederiz.
    #     # *  ile ** ayni degildir.

    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.number = validated_data.get('number', instance.number)
    #     # burada bir ternary if mantigi var. eger validated data nin icinde yeni bir veri geldi ise ve o veri hangi field da degisiklik sonucu olustuysa o field in yeni hali o olacak. eger degisiklik yapilmadi ise instance.number seklinde yazilan eski hali olacak.

    #     instance.save()
    #     return instance






#################  Model Serializer:

## Burada create ve update methodlari yazmiyoruz. django geri planda hallediyor.

## Note: Gün hesaplamak icin; SerializerMethodField  kullandik. Bu method, serializer in herhangi bir yerinde calistirilir ve db de hicbirsey kaydetmez. direkt olarak kullaniciya veri dönüsü yapar. Bu nedenle db ye yük bindirmez.

class StudentSerializer(serializers.ModelSerializer):
    
    days_since_joined = serializers.SerializerMethodField() ## gün hesaplamak icin
    #### Önemli: fields kismina asagidaki func ismi get_days_since_joined eklenmez. Burada tanimladigimiz fields ismi eklenir.
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "number", "path" ,"register_date", "days_since_joined"]
        # fields = "__all__"
        # exclude = "id"

    ## Bu islemin adi field level validation. Docs da baska validationlarda var.
    def validate_first_name(self, value):
        """
            Check that the number is below 1000
        """
        # if value > 1000:
        #     raise serializers.ValidationError("Numbers must below 1000")
        if value == "rafe":
            raise serializers.ValidationError("error")   
        return value

    ## gün hesaplama:
    def get_days_since_joined(self, obj):
        # return (now() - obj.register_date).days
        return (now() - obj.register_date).seconds

## girilen number 1000 in altinda ise db ye yeni eleman ekler. yoksa eklemez hata verir.







## burada PathSerializer icinde isim olarak students kullanmamizin nedeni; model de student modelin de foreign key ile baglama yaparken,  related_name in students olmasidir. burada kullanirken student bile yazsak hata aliriz.
        
class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = "__all__"

    ## iki serializer i birbirine baglamak icin 3 tane yöntem ögrendik:
    ## 1. Yöntem:
    ## nested serializer yapisi icin sadece bunu yapmak yeterli.
    # students = StudentSerializer(many = True)
    ## many = True demek bir path altina birden cok ögrenci gelebilir demek. 
    ## Önemli: student tablosunda zaten path diye bir field oldugu icin normal de biz student lere ait path leri serializer vasitasi ile user a verebiliyoruz. Ama biz burada nested seria yapmaya calisiyoruz. Yani mesela 1 numarali path e ait user larin hepsi onun altinda olsun istiyoruz. Normal de path modelinde student diye bir field yok ve bu nedenle normalde paths/ endpoint i altinda kullaniciya student isimlerini veremiyoruz. Buna ragmen, student modelindeki related_name i kullanarak; PathSerializer ile user lara student isimlerini verebiliyoruz.  
    ## Bu yöntemi kullandigimizda; path altindaki student da user a hangi verileri sunariz:
    ## StudentSerializer da fields olarak neler tanimlanmis ise onlari


    ## 2. Yöntem:
    ## stringRelatedField:
    ## StringRelatedField  kullandigimizda StudentSerializer ile yada student modeli ile baglamak icin herhangi birsey belirtmiyoruz. buna ragmen kendisi related_name den kaynakli bir baglanti sagliyor. ve baglanti student modeli ile saglandigi icin; veri olarak student tablosunun return ettigi __str__ dönüyor.
    ## StringRelatedField kullandigimizda integer veri de hata veriyor.
    # students = serializers.StringRelatedField(many=True)



    ### 3. Yöntem:
    #PrimaryKeyRelatedField:
    students = serializers.PrimaryKeyRelatedField(read_only = True, many = True)

## Bu yöntemi kullandigimizda su sekilde bir veri elde ederiz:
    # {
    #     "id": 2,
    #     "students": [
    #         3,
    #         4
    #     ],
    #     "path_name": "be"
    # }

## Burada; "id" bizim tablomuzda backend path i ne ait id dir. altindaki student lar; backend pathinde olan student lardir. ama PrimaryKeyRelatedField kullandigimiz icin; student larin isim ve soyisimleri gelmez; sadece student tablosunda primary key olan id ler gelir. 
    




## Note: field lar icinde kullanilan read_only ve write_only:

## read_only ye örnek;  id field idir. Biz ne yaparsak yapalim django kendisi bir id atar. Cünkü default olarak read_only dir id field. Yani okuma esnasinda gösterilir ama create ve update kisminda gösterilmez.

## write_only de ise biz bu field icin create ve update asamasinda bilgi girisi yapabiliriz ama user a gösterilmez representation kisminda.

## baska arguments larda vardir: link
## https://www.django-rest-framework.org/api-guide/fields/#serializer-fields