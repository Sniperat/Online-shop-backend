from django.contrib import admin
from .models import AbstractUser

admin.site.registration(AbstractUser)
# Register your models here.
