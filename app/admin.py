from django.contrib import admin
from .models import Category , Product,Image,AttributeKey,AttributeValue,ProductAttribute
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    
    
admin.site.register(Product)

admin.site.register(Image)


admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)


