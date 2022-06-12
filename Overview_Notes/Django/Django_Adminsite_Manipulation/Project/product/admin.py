from django.contrib import admin
from .models import Product, Review, Category
from django.utils import timezone
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from product.resources import ReviewResource
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

# biz detay page e girince zaten edit yapabiliyoruz. Biz burada list sayfasini edit ediyoruz.

class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20



### burada ismi ProductAdmin olmasa da calisiyor.
class ProductAdmin(admin.ModelAdmin):
    

    # list_display = ("name", "create_date", "is_in_stock", "how_many_reviews" ,"update_date")
    list_editable = ( "is_in_stock", )
    # list_display_links = ("create_date", "name")

    list_filter = ("is_in_stock", "create_date")
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter))

    ## alfabetik siralama
    ordering = ("name",)

    search_fields = ("name",)

    prepopulated_fields = {'slug' : ('name',)}

    list_per_page = 15

    date_hierarchy = "update_date"

    # fields = (('name', 'slug'), 'description', "is_in_stock")

    inlines = (ReviewInline,)  ## ReviewInline  i  baglamak icin kod


    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")

    bring_img_to_list.short_description = "product_image"


    ## bölümler basligi degisebilir.
    fieldsets = (
        ("Bölümler", {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ), # acilip kapanan
            #"classes" : ("wide", ), # normal her zaman acik
            #"classes" : ("extrapretty", ), # daha genis 
            "fields" : ("description", "categories", "product_img", "fotograf"),
            'description' : "You can use this section for optionals settings"
        })
    )

    filter_horizontal = ("categories", )
    # filter_vertical = ("categories", )

    readonly_fields = ("fotograf",)

    ## delete haricinde action ekleme
    actions = ("is_in_stock", )  ## öncelikle bu yazilir.

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'


    list_display = ("name", "create_date", "is_in_stock", "update_date","added_days_ago", "how_many_reviews", "bring_img_to_list")    
	
    def added_days_ago(self, product):
        day = timezone.now() - product.create_date
        return day.days




## normalde her bir register satirinda bir tane model yazabiliyoruz.
### biz burada parantez icine, ProductAdmin de yazarak bizim Product modelimizi manipule edebilmeyi sagladik.
## eger ProductAdmin  i  Burada kullanmazsak calismaz.
admin.site.register(Product, ProductAdmin)




################################
class ReviewAdmin(ImportExportModelAdmin):
    ## review eklerken product secmemiz gerekir. tek tek isim aramamak icin search bar ekleme
    autocomplete_fields = ("product",)
    list_display = ('__str__', 'created_date', 'is_released')
    ## bu kod ile, review in list sayfasinda bulunacak bilgiler düzenlenir. review in detay sayfasindaki bilgiler degil.

    list_per_page = 50
    # raw_id_fields = ('product',) 
    resource_class = ReviewResource


## Bu kod filter dropdown icin

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'created_date', 'is_released')
#     list_per_page = 50
#     list_filter = (
#         ('product', RelatedDropdownFilter),
#     )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)




# Bu kod browser in tab in da bulunan title i degistirir
admin.site.site_title = "Tarik's Webpage"



## Admin page de baslik olan Django administration  ismini degistirmek
admin.site.site_header = "Tarik's Admin Page"



#Site administration isimli basligi degistirmek:
admin.site.index_title = "Tarik's Administration"


