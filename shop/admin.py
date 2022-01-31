from django.contrib import admin
from .models import ProductModel, CategoryModel

admin.site.registration(ProductModel)
admin.site.registration(CategoryModel)

# Register your models here.
