from django.urls import path
from .views import (
    CategoryListApiView,
    ChildCategoryByParentSlug,
    GetProductsByChildCategory,
    ProductList,
    GetProductAPIView,
    ProductAttributeListAPIView
    )
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'attributes', ProductAttributeListAPIView, basename='attributes')

urlpatterns = [
    path('',CategoryListApiView.as_view()),
    path('category/<slug:parent_slug>/',ChildCategoryByParentSlug.as_view()),
    path('category/<slug:parent_slug>/<slug:child_slug>/',GetProductsByChildCategory.as_view()),
    path('products/',ProductList.as_view()),
    path('products/<int:pk>/',GetProductAPIView.as_view()),
    
] + router.urls