from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255,unique=True)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(null=True,blank=True)
    
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        if self.parent:
            return f"{self.parent.title} → {self.title}"
        return self.title
    
    class Meta:
        verbose_name_plural = 'categories'
    



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='products',
                                 null=True)
    def __str__(self):
        return self.name


# product.images.all()

class Image(models.Model):
    image = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                related_name='images',
                                null=True
                                )
    
    def __str__(self):
        return f'{self.product.name} - {self.image.url}'


class AttributeKey(models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name
    

class AttributeValue(models.Model):
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    attribute_key = models.ForeignKey(AttributeKey,on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_attributes')
    
   