### PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django

python -m django --version
django-admin startproject core .

pip install python-decouple
pip freeze > requirements.txt
```
add a gitignore file at same level as env folder

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.

go to terminal, stop project, add app

```
py manage.py startapp products
```

go to settings.py and add 'products' app to installed apps 


---------------------------------------------------------------------------------------------------

products/models.py

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
	is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
```

* makemigrations and migrate
* createsuperuser

products/admin.py

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)



# Bu kod browser in tab in da bulunan title i degistirir
admin.site.site_title = "Clarusway Title"



## Admin page de baslik olan Django administration  ismini degistirmek
admin.site.site_header = "Clarusway Admin Portal"  



#Site administration isimli basligi degistirmek:
admin.site.index_title = "Welcome to Clarusway Admin Portal"
```

Add data with Faker package:
Bu paket bize damy data saglar. Modellerimizde ve db mizde template lerimizde kullanmak icin

* pip install Faker
# Bu projede pip ile baslayan komutlar calismiyor. o nedenle pip ile baslayan tüm komutlarin baslarina, python -m pip install Faker olarak yaziyorz. diger tüm komutlarda da bu sekilde.

## faker documentation:
https://faker.readthedocs.io/en/master/

py manage.py shell
go to shell:
```bash
from product.models import Product
from faker import Faker

## burada faker class indan bir faker instance i  yani object i olusturuyoruz.
faker = Faker()

for i in range(1,200):
	product = Product(name=faker.name(),description=faker.paragraph(),is_in_stock=False)
    # bu satir yerine Product.objects.create diyerek save den kurtulabilirdik. 
    # burada yaptigimiz islem, model den orm vasitasi ile instance üretmektir.

	product.save()
## Note:  
## shell de; faker.name() komutunu her calistirdigimizda yeni bir isim üretir.  
## faker.paragraph()  komutunu her calistirdigimizda ise yeni bir fake description üretir.
## faker.address()
## faker.text()
#  faker.sentence()

# for _ in range(10):
#   print(fake.name())   10 tane isim üretir.
# buradaki _  kullanilmayacak i ler icin yazilir


# from faker import Faker
# fake = Faker('tr_TR')
# for _ in range(10):
#     print(fake.name())
## bu komut locallestirme yapar ve 10 tane türk isim üretir.

## bir seferde birden cok ülkede girilebilir
# from faker import Faker
# fake = Faker(['it_IT', 'en_US', 'ja_JP'])
# for _ in range(10):
#     print(fake.name())

- eger model tanimlama esnasinda is_in_stock = False deseydik default olarak false yapardi ve burada tekrar yazmak zorunda kalmazdik.
```

go to admin site and check data 




#############
How to create a Dynamic Provider
Disaridan kendi girdigimiz verileri de faker in elementleri haline getirebiliriz.
Dynamic providers can read elements from an external source.

from faker import Faker
from faker.providers import DynamicProvider

medical_professions_provider = DynamicProvider(
     provider_name="medical_profession",
     elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(medical_professions_provider)

# now you can use:
fake.medical_profession()
# 'dr.'






How to customize the Lorem Provider
You can provide your own sets of words if you don’t want to use the default lorem ipsum one. The following example shows how to do it with a list of words picked from cakeipsum :

from faker import Faker
fake = Faker()

my_word_list = [
'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat' ]

fake.sentence()
# 'Expedita at beatae voluptatibus nulla omnis.'

fake.sentence(ext_word_list=my_word_list)
# 'Oat beans oat Lollipop bar cheesecake.'


-------------------------------------------------------------------------------------------------










### ModelAdmin options and methods

modelAdmin:
got to django admin site document and modelAdmin source 


some modelAdmin options:

```python

# asagidaki kodlari admin.py da yaziyoruz

### Note: burada yaptigimiz islemler, admin panelde degisiklik yapar. bizim kendi olusturdugumuz template lere tesir etmez.

## admin.py da yazdigimiz kod da ModelAdmin  üzerine ctrl ile tiklarsak, default olarak nasil yazildigini görürüz. Burada biz manipule edecegiz.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    # bunun icin default model deki __str__ de yazili olan veriler

    list_editable = ( "is_in_stock", )
    ## veri degistirme imkani verir. ama en son save e tiklamamiz gerekir.

    list_display_links = ("create_date") 
    # #can't add items in list_editable to here, yani hem editable hem de link yapilamaz ikisinden biri secilmesi gerekir.
    ## default olarak admin panel de bizim isimlerimizin üzerine tiklanabiliyor ve bunlarin link özelligi var. ama burada degistirilebilir.

    # filtreleme
    list_filter = ("is_in_stock", "create_date")

    ## alfabetik siralama
    ordering = ("name",)  

    ## search bar cikarir karsimiza arama da kolaylik saglar.
    search_fields = ("name",)

    ## biz yeni bir product eklerken, name yazma esnasinda name ile ayni olacak sekilde otomatik olarak slug üretir. eskiden olusmus product lara tesir etmez.
    prepopulated_fields = {'slug' : ('name',)}  

    ## her sayfada kac product
    list_per_page = 25

    ### date e göre siralama saglar. search bar in altinda tiklanabilen date ler cikar. Hangi date e basarsak o date de olan veriler gelir.
    date_hierarchy = "update_date"


    ### Burada tek bir tuple icine konulan veriler tek satirda bulunur yada birbirlerine yakin bulunurlar, digerleri ise ayri ayri satirlarda bulunur.
    fields = (('name', 'slug'), 'description', "is_in_stock") 
    #fieldset kullandığımız zaman bunu kullanamayız

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )



admin.site.register(Product, ProductAdmin)

```

actions section:
## 
Normalde action kisminda sadece delete vardir. biz extra eklemek icin custom func yazariz.

```python

   actions = ("is_in_stock", )  ## öncelikle bu yazilir.

   def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
   is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
```



Add methods to modelAdmin:
Model de bulunan field larimiz haricinde bir alan ekleyecegiz.
ekleme yapacagimiz icin list_display  i  yeniden yazacagiz.

```python
		list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago")    
	
	    def added_days_ago(self, product):
        	day = timezone.now() - product.create_date
        	return day.days
```


-----------------------------------------------------------------------------------------------------




### RichText Editors

Bu, admin panel de, product in detay kismindaki editörü sekillendirir.
Bu editör ile harfleri bolt yapabiliriz alti cizili olabilir emoji eklenebilir.

    WYSIWYG (what you see is what you get)

    https://djangopackages.org/grids/g/wysiwyg/
    https://django-ckeditor.readthedocs.io/en/latest/

* pip install django-ckeditor

* 'ckeditor',      >>> add installed_apps   settings.py

models.py
```Python
    from ckeditor.fields import RichTextField

    description = models.TextField(blank=True)  ## eski hali 
    >>>> description = RichTextField()  ## yeni hali
```

* makemigrations and migrate

* for extra config go to settings.py

settings.py
```Python
    CKEDITOR_CONFIGS = {
        'default' : {
            'toolbar' : 'full',  ## arac cubugunda hersey olur
            'height' : 700,
            'width' : 1000
        }
    }
```
* Note: ilgili template dosyasında: {{description | safe}}
#########  normalde emojiler felan db ye yüklenmez. bu son kod, emoji tarzi seylerin db ye yüklenmesini saglar. 




-----------------------------------------------------------------------------------------------------





### Model Relations 

* Add new model:

models.py
```python
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"  
```

* makemigrations and migrate

admin.py
```Python
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 

admin.site.register(Review, ReviewAdmin)
```

shell
```
from product.models import Product, Review
from faker import Faker
faker = Faker()

## buradaki iterator, objects.all un diger yöntemidir. iterator ile veri iterable olur.
for product in Product.objects.iterator():
    reviews = [Review(review=faker.paragraph(), product=product) for _ in range(0,4)]
    ## bu kod da list comprahansion yapisi vardir. bir liste icinde ayni anda 4 tane Review modelinden intance üretilir ve bir liste icine atilir. buradaki product = product daki product for döngüsünden gelir. yani i yerine 

    ## bulk_create methodu ise for ile olusturulan 4 tane objecti ayni anda create eder. ve tek tek degil hepsini ayni anda db ye kaydeder.
    Review.objects.bulk_create(reviews)

    ## buradaki tüm islemler sonucunda 800 tane review kaydedilir. 200 tane product ve 4 tane objenin carpimi.

Review.objects.count()
```




### TabularInline

Su ana kadar yazdigimiz kodlar sonucunda;  biz product ve review kaydetme islemlerini ayri ayri yapmak zorundayiz. Simdi product create ederken, bir pencere daha acilmasini ve bu pencere ile ayni zamanda review de kaydetmeyi istiyoruz.
Yani modeller arasinda parent child iliskisi saglar. product parent modelinden yeni bir product üretirken, ayni zamanda child modeli olan review den de birsey secmemizi saglar.

Kurulum:  child olan model yani burada ReviewInline, TabularInline  dan türetilir. Bunun model kismina, models.py da olusturudugumuz Review  modeli yazilir. Daha sonra parent modelin icerisine inlines = (ReviewInline,)  yazilir ve tamamlanir.

admin.py
```Python
bu admin.py da ProductAdmin üzerine yazilir. 

class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1  # admin panelde + tusu cikar ve her bastigimizda bir tane extra ekler
    classes = ('collapse',)
    # min_num = 3  ## bu bir product icin en az 3 review eklemeye zorlar
    # max_num = 20  ## bu da bir product icin maximum 20 review

## bu kodun sadece icindeki kisim alinarak ProductAdmin  icinde herhangi bir yere yapistirilir.

class ProductAdmin(admin.ModelAdmin):
    inlines = (ReviewInline,)
```








### custom fields

models.py
```Python

# Bu kod models deki product modlei icine yazilir.
class Product(models.Model):        

    def how_many_reviews(self):
        count = self.reviews.count()
        return count
```

* add productAdmin >>> list_display icine bu eklenir ("how_many_reviews")









### horizontal & vertical filter (ManytoMany Field)

mesela product olustururken category secenegi olustururuz. category secerken, normal de ctrl ye tiklayarak birdn cok secme yapabiliriz. bu kod ile choose all gibi farkli secenekler sunar bize.

models.py
```Python

models.py da yeni bir category olustururuz. ancak product ile iliski kurulacagi icin product modeli üzerine yazilir.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name


# product icinde bu kod yazilarak iki model arasinda iliski saglanir.
class Product(models.Model):
    ...
    categories = models.ManyToManyField(Category, related_name="products")
```

* makemigrations and migrate

admin.py
```Python
from .models import Product, Review, Category

# admin.py da bulunan fieldsets e sadece categories kismi eklenerek calistirilir. sadece fields kismina eklemek zorunda degiliz. baska bir kisma da eklenebilir.
Biz burada Optionals Settings kismina ekledik. Bu nednele bu da collapse oldugu icin eklemek icin collapse acilir.


    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories"),
            'description' : "You can use this section for optionals settings"
        })
    )
    # filter_horizontal = ("categories", )
    filter_vertical = ("categories", )

admin.site.register(Category)

## tabi ki product da secim yapabilmek icin önce birkac category olusturuyoruz.
```








# Display Image Fields

Normalde admin page de image lerimiz görünmez. sadece linkleri görünür. simdi yazacagimiz kod ile image larimizi görecegiz.

settings.py da asagidaki kodlar yazilir.
bu kodlar yazilinca os u da orada import etmemiz gerekecek.
birde STATICFILES_DIRS icinde staticfiles yazdigimiz icin bunu arayacaktir. Bu nedenle ana dizinde staticfiles adinda bir klasör olusturulur. aksi takdirde warning verir

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

# dikkat: asagidaki kod ana projenin urls.py icin
url.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]
#yukaridaki kisim zaten urls.py da var. biz alttaki kismi ekleriz.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

models.py
```python


## asagidaki kod, product modeli icine eklenir.
product_img = models.ImageField(null=True, blank=True, default="defaults/default.png", upload_to="product/")

# Burada default image kullanacagiz. Bunun icin yukarida MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  kodunu yazdigimiz icin; ana dizinde bir media klasörü olustuuracagiz. bunun altinda da defaults klasör.

# dikkat default image i static e koymuyoruz. media ya koyuyoruz cünkü bizim upload ettiklerimiz ile alakali 

## normalde django da html tag leri gönderemiyoruz. Bu nedenle normal bir gönderimde bize hata verir. ama burada mark_safe kullanarak django ya diyoruz ki; bu güvenli birsey sikinti cikarma diyoruz.


models.py da

from django.utils.safestring import mark_safe

    def bring_image(self):
        if self.product_img:
            return mark_safe(f"<img src={self.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{self.name} has not image </h3>")
        ## eger resim yoksa bu yazi döner.
```

* pip install pillow
* makemigrations and migrate

admin.py
```python
readonly_fields = ("bring_image",)
## resimi görebilmek icin bunu ProductAdmin icinde yapmak zorundayiz.

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories", "product_img", "bring_image"),
            'description' : "You can use this section for optionals settings"
        })
    )
```

su ana kadar ki kodlar, product in detay sayfasinda foto göstermek icindi.
simdi listede image gösterme:

admin.py
```python
from django.utils.safestring import mark_safe

    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")

	list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews", "bring_img_to_list") 
    
    # eger daha anlamli bir isim vermek istersek asagidaki kod admin.py da kullanilir:
    bring_img_to_list.short_description = "product_image" 
```

--------------------------------------------------------------------------------------









# Customize templates

### Önemli:
Biz normalde ana dizinde templates diye bir klaösr olusturmadan, direkt olarak env altindaki klasörlere gidip oradaki html yada css kodlarinda degisiklik yapabilirz. ama bu durumda tüm degisiklikler bizim localimizde kendi env imizde olur. yani github a push ettigimizde kisiler kendi env lerini yüklediklerinde hicbir sey göremezler. Bu nedenle biz ana dizinde templates olusturuyoruz ve böylece degisiklikler her yerde calisiyor. 
ve biz env deki default template leri overwrite ediyoruz.

simdi django tarafindan bize saglanan template leri customize edecegiz.

default directory : env/lib/django/contrib/admin/templates/admin
klasörler kisminda bu yolu takip ettigimizde template leri buluruz.
Asagidaki sayfalyarda degisiklik yapmak icin karsilarinda bulunan template leri overwrite etmemiz gerekir.

Liste Sayfası -> admin/change_list.html  # listede degisiklik icin

Ekleme ve Güncelleme Sayfaları -> admin/change_form.html  
(ekleme güncelleme dedigimiz; product modelinin ana sayfasi yani add butonunun oldugu kisim ve güncelleme kismi ise product i güncelledigimiz detay sayfasi. ikisi de ayni template den ihrerit edilmis djanfo template lerde. Bu nedenle ikisinin degisikligi icinde de admin/change_form.html  de degisiklik yapilir.)

Silme İşlemi İçin Onay Sayfası -> admin/delete_confirmation.html

Modelin Geçmişi -> admin/object_history.html  (Bir product in yani bir object in üzerine tikladigimizda, detay sayfasinda sag üstte History yazar. Buraya tikladigimizda bu object üzerinde en son kimlerin neler yaptigini yazar. Bu sayfayi degistirmek istersek admin/object_history.html sayfasini overwrite edecegiz)

## admin ana sayfada degisiklik
admin/<extend_edilecek_sablon_adi>.html     >>>>>>> admin site ana sayfa

## app de degisiklik
admin/<app_adi>/<extend_edilecek_sablon_adi>.html   >>>>>>>>> applere özel


## model de degisiklik
admin/<app_adi>/<model_adi>/<extend_edilecek_sablon_adi>.html  >>>>>>>>>> modellere özel



### Note:

    'DIRS': [],
    'APP_DIRS': True,  
    normalde settings.py da default kod bu sekildedir. Bu ne demek. 
    'DIRS': [],  bu kod ana dizinde template yok sen 'APP_DIRS': True, kodu ile app ler icindeki template leri oku demek.
    ama biz simdi ana dizine template yazacagiz ve öncelikle bunu okumasini isteyecegiz. Bu nedenle asagidaki kod kullanilir. ve ana dizinde templates folder olusturacagiz.

settings.py:
```python
'DIRS': [BASE_DIR, "templates"],
```
ilk önce buraya bakar yoksa defaulta gider, default da app ler altindakilerdir


# ana dizinde bu klasörler olusturulur.
templates/admin/product(app ismi)/product(model ismi)/change_form.html

** içi boş olduğu için Ekleme ve Güncelleme Sayfaları boş görünecek

** default olan change_forma gidip blockları bakabiliriz istediğimizi güncelleriz extend edip
```html
{% extends 'admin/change_form.html' %}

## bunu nereden aliyoruz?
## env/lib/django/contrib/admin/templates/admin  bu yolu takip ettigimizde templatelerin icinden aliriz.

## django tüm template leri block lar haline getirmistir. 
## bizde degisikliklerimizi yapmak istedigimiz zaman env icindeki template lere gidip bakarak yapiyoruz.

{% block form_top %}
    <h1>Product model new template</h1>
{% endblock  %}
```

-----------------------------------------------------------------------




## admin page in kendisinde degisiklik yapacagiz:



admin templates extends hierarchy: (yani admin ana sayfasinin template i bu siralamaya göre extends eder.)
base.html > base_site.html > change_form.html

## ana dizindeki templates de su klasörler acilir:

templates/admin/base_site.html

## logo da kullanacagimiz foto static dir media degil.
img directory :  contrib/admin/static/admin/img/clarusway.png
add clarusway.png to this directory


## admin altindaki base_site.html e bu kodlar yazilir.
base.html herseyin baslangicidir. Tüm template ler buradan inherit edilir. Bu nedenle burada cok degisiklik yapmayiz.

bizim projede, mesela  change_form.html  base_site dan  base_site ise base.html den miras alir.


```html
{% extends 'admin/base.html' %}
{% load static %}


{% block branding %}
    <div class="myDiv">
    <img src="{% static 'admin/img/clarusway.png' %}" style="height: 50px; width: 50px;" alt="">
    <h1 id="head">
        Clarusway Admin Site
    </h1>
    </div>
{% endblock %}
{% block extrastyle %}
    <style>
        #header {
            height: 50px;
            background: #542380;
            color: #fff;
        }

        #branding h1 {
            color: #fff;
        }

        a:link,
        a:visited {
            color: #10284e;
        }

        div.breadcrumbs {
            background: #542380;
            color: #10284e;
        }

        div.breadcrumbs a {
            color: #333;
        }

        .module h2, .module caption, .inline-group h2 {
            background: #542380;
        }

        .button, input[type=submit], input[type=button], .submit-row input, a.button {
            background: #10284e;
            color: #fff;
        }
        div.myDiv {
            display: flex;
            align-items: center;
        }

    </style>
{% endblock %}
```




# THIRD PARTY PACKAGES



### List-Filter Dropdown
sag üst köse de bir dropdown cikar ve neye göre filtreleme yapmak istersek ona göre filtreleme yapar. Biz burada product a göre yaptik


* https://github.com/mrts/django-admin-list-filter-dropdown

pip install django-admin-list-filter-dropdown

INSTALLED_APPS = (
    ...
    'django_admin_listfilter_dropdown',
    ...
)

admin.py
```python

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    list_filter = (
        ('product', RelatedDropdownFilter),
    )
```






### Django admin date range filter

Daha önce biz product admin sayfasinda iki tane filter eklemistik ve bunlar sayfanin sag üst kösesinde calisiyordu. is in stock ve create date icin.
Simdi yazacagimiz kod ile; create date icin olusan filter da tarih secmek icin date picker olusacak ve tarihi oradan sececegiz.

Ama admin.py da eski list filter in üstte kalmasina yada bunun comment e alinmasi gerekir.
    list_filter = ("is_in_stock", "create_date")  ## eskisi
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter)) ## yenisi

https://github.com/silentsokolov/django-admin-rangefilter

* pip install django-admin-rangefilter

INSTALLED_APPS = (
    ...
    'rangefilter',
    ...
)

admin.py

```Python
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class ProductAdmin(admin.ModelAdmin):
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter)) 
    # modelde datetimefield kullandığımız için
```









### import - export

Bu özellik; bizim dosyalarimizi disari export etme imkani ve disaridan bizim dosyamiza baska dosyalar import etme imkani sunar.

https://django-import-export.readthedocs.io/en/latest/

* pip install django-import-export

INSTALLED_APPS = (
    ...
    'import_export',
)

product app icinde resources.py isimli bir dosya olusturuyoruz.
```python

resources.py icinde:

from import_export import resources
from product.models import Review

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review # default all fields
        # fields = ("is_released", "product")    
```

admin.py
```python
from import_export.admin import ImportExportModelAdmin
from product.resources import ReviewResource


## Normalde ReviewAdmin kodu su sekilde idi:
## class ReviewAdmin(admin.ModelAdmin)
## simdi biz bu kodu degistirecegiz yani ImportExportModelAdmin  den üretecegiz:

class ReviewAdmin(ImportExportModelAdmin):

    resource_class = ReviewResource
```

### Not:
biz review da bu kodlari yazdigimiz icin import export islemleri sadece orada olur su an icin.









### custom template (grapelli)

Siyah beyaz ve farkli bir arayüz saglar. Ilave özellikler katar. Docs da detayli anlatiliyor.

https://django-grappelli.readthedocs.io/en/latest/

* pip install django-grappelli

INSTALLED_APPS = (
    'grappelli',    # en üstte olacak
    'django.contrib.admin',   ## bu zaten default var
)


from django.conf.urls import include
urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS üstte olacak
    path('admin/', admin.site.urls), # admin site
]



