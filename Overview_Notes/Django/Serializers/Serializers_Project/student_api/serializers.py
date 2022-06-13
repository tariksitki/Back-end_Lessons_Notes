

from rest_framework import serializers
from .models import Student, Path
from django.db import models

## Note: serializer kisminda, model de olusturdugumuz class a ait field lari gösterebiliriz. Eger model de olmayan bir field i seria da göstermek istersek hata aliriz.


# burada StudentSerializer altinda belirledigimiz isimler bizim dönüstürmek istedigimiz verilerdir. Bu veriler json a dönüsecek. Bunu serializers yapacak.
# Ayrica bunlarin view da öncelikle islemleri yapilacak, daha sonra url.py da kullanicinin son görecegi hale gelecek.
class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    number = serializers.IntegerField()

    # Not: Normalde models.py da 5 tane field var. ama biz burada 3 tanesini json a dönüstürdügümüz icin, kullanici 3 tane field görüyordu. Bir buna ilave olarak birde id görsün istiyoruz. Models de id yok ama django kendisi db de otomatik olusturur. simdi biz bu hazir id yi user a sunuyoruz.
    # id = serializers.IntegerField()

    # su ana kadar yazdigimiz kodlar ile sadece json formatinda okuma islemi yapabiliriz. Eger template de post islemi yapmak istersek hata aliriz. Bu nedenle simdi asagidaki kodlari yazacagiz:

    def create(self, validated_data):
            return Student.objects.create(**validated_data)
        ## eger user tarafindan girilen veri validated ise, bu bilgiler ile yeni bir veri create ederiz.
        # *  ile ** ayni degildir.

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        # burada bir ternary if mantigi var. eger validated data nin icinde yeni bir veri geldi ise ve o veri hangi field da degisiklik sonucu olustuysa o field in yeni hali o olacak. eger degisiklik yapilmadi ise instance.number seklinde yazilan eski hali olacak.

        instance.save()
        return instance




























# from rest_framework import serializers
# from .models import Student
# from django.utils.timezone import now

# # class StudentSerializer(serializers.Serializer):
# #     first_name = serializers.CharField(max_length=50)
# #     last_name = serializers.CharField(max_length=50)
# #     number = serializers.IntegerField()
# #     # id = serializers.IntegerField()

# #     def create(self, validated_data):
# #         return Student.objects.create(**validated_data)

# #     def update(self, instance, validated_data):
# #         instance.first_name = validated_data.get('first_name', instance.first_name)
# #         instance.last_name = validated_data.get('last_name', instance.last_name)
# #         instance.number = validated_data.get('number', instance.number)
# #         instance.save()
# #         return instance




# class StudentSerializer(serializers.ModelSerializer):
#     days_since_joined = serializers.SerializerMethodField()
#     class Meta:
#         model = Student
#         fields = ["id", "first_name", "last_name", "number", "days_since_joined", "register_date"]

#     def validate_number(self, value): 
#         """ Check that the blog post is about Django. """ 
#         if value > 1000 : 
#             raise serializers.ValidationError("Number must be below 1000!!!") 
#         return value

    
#     def get_days_since_joined(self, obj):
#         return (now() - obj.register_date).days
    






# is_valid() dediğimizde bu metotlar çalışıyor



# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'first_name', 'last_name', 'number')
#         # fields = '__all__'
#         # exclude = ('id',)


