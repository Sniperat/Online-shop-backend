from django.shortcuts import render
from .models import ProductModel, CategoryModel
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class CategoryView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = CategoryModel.objects.all()
        serializers = CategorySerializer(categories, many=True)

        return Response({
            'status': 'success',
            'data': serializers.data
        })


class ProductView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        products = ProductModel.objects.all()
        serializers = ProductSerializer(products, many=True)

        return Response({
            'status': 'success',
            'data': serializers.data
        })


