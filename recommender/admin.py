from django.contrib import admin
from .models import Recommendations
from .models import Products

# Register your models here.

admin.site.register(Recommendations)
admin.site.register(Products)


