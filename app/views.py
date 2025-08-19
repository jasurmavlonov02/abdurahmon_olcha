from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Category, Product,ProductAttribute
from .serializers import (
    CategoryModelSerializer,
    ProductModelSerializer,
    ProductDetailSerializer,
    ProductAttributeSerializer
)
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action






# class CategoryListApiView(APIView):
#     def get(self,request):
#         categories = Category.objects.all()
#         serializer = CategoryModelSerializer(categories,many=True,context={'request':request})
#         return Response(serializer.data)
    
class CategoryListApiView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.filter(parent__isnull = True)
    
    


class ChildCategoryByParentSlug(ListAPIView):
    serializer_class = CategoryModelSerializer
    
    def get_queryset(self):
        parent_slug = self.kwargs['parent_slug']
        try:
            parent = Category.objects.get(slug = parent_slug)
        except Category.DoesNotExist:
            parent = None
            raise NotFound(detail="Parent category not found")
        
        return parent.children.all()
    
    

class GetProductsByChildCategory(ListAPIView):
    serializer_class = ProductModelSerializer
    
    def get_queryset(self):
        parent_slug = self.kwargs['parent_slug']
        child_slug = self.kwargs['child_slug']
        # category = Category.objects.get()
        parent_category = get_object_or_404(Category,slug=parent_slug,parent__isnull = True)
        child_category = get_object_or_404(Category,slug=child_slug,parent = parent_category)
        
        return Product.objects.filter(category = child_category)
    
    
class ProductList(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    
class GetProductAPIView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    
    
class ProductAttributeListAPIView(viewsets.ModelViewSet):
    serializer_class = ProductAttributeSerializer
    queryset = ProductAttribute.objects.all()

    @action(detail=False, methods=["get"],url_path="product/(?P<product_id>[^/.]+)")
    def by_product(self,request,product_id = None):
        product_attributes = self.queryset.filter(product = product_id)
        serializer = self.get_serializer(product_attributes,many=True)
        return Response(serializer.data)
        

    



