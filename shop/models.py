from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from self import self


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])
        # return reverse('shop:products_by_category', kwargs={'slug':self.slug})

    


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=CASCADE)
    img = models.ImageField(upload_to='product',blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:prodCatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
