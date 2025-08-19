from rest_framework.serializers import ModelSerializer,Serializer,SerializerMethodField
from .models import Category, Product,Image,ProductAttribute

      
class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = Image     
        exclude = ()
    
class ProductModelSerializer(ModelSerializer):
    primary_image = SerializerMethodField()
    image_count = SerializerMethodField()
    
    def get_image_count(self,obj):
        return obj.images.count()
    
    def get_primary_image(self,obj):
        request = self.context['request']
        first_image = obj.images.first()
        if first_image and request:
            return request.build_absolute_uri(first_image.image.url)
        elif first_image:
            return first_image.image.url
        return None

       
       
    class Meta:
        model = Product
        exclude = ()
        
class ProductDetailSerializer(ModelSerializer):
    images = ImageModelSerializer(many=True,read_only = True)
    class Meta:
        model = Product
        exclude = ()
    
        
        
class CategoryModelSerializer(ModelSerializer):
    # products = ProductModelSerializer(many=True,read_only = True)
    class Meta:
        model = Category
        exclude = ()
        

class ProductAttributeSerializer(ModelSerializer):
    class Meta:
        model = ProductAttribute
        exclude = ()
        