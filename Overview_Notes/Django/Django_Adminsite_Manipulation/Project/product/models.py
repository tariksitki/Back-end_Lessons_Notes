from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe





class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name






class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name="products")
    product_img = models.ImageField(null=True, blank=True, default="defaults/default.jpg", upload_to="product/")
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    description = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


    def __str__(self):
        return self.name

    def how_many_reviews(self):
        count = self.reviews.count()
        return count
    ## bunu görebilmek icin admin.py da list e eklememiz gerekir
    # eger Review de related_name='reviews' tanimli olmasaydi, count = self.review_set.count()  seklinde kullanmamiz gerekirdi.


    def fotograf(self):
        if self.product_img:
            return mark_safe(f"<img src={self.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{self.name} has not image </h3>")


  






class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    ## related_name='reviews',  product da how_many_review icin kullanacagiz.
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}" 