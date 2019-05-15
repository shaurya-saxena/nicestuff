from django.contrib import admin
from .models import Products
from .models import Recommendations
from .models import TxnHistory



# Register your models here.

admin.site.register(Products)
admin.site.register(Recommendations)
admin.site.register(TxnHistory)



