from .models import CategoryModel, ProductModel
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
