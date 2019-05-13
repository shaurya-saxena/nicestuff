from django.contrib import admin
from .models import Products
from .models import RecommendationsMA
from .models import RecommendationsWA
from .models import RecommendationsTech
from .models import RecommendationsHD
from .models import RecommendationsFurn
from .models import RecommendationsWF
from .models import RecommendationsBPC
from .models import RecommendationsKD
from .models import RecommendationsAccs
from .models import RecommendationsMF
from .models import TxnHistory



# Register your models here.

admin.site.register(Products)
admin.site.register(RecommendationsMA)
admin.site.register(RecommendationsWA)
admin.site.register(RecommendationsTech)
admin.site.register(RecommendationsHD)
admin.site.register(RecommendationsFurn)
admin.site.register(RecommendationsWF)
admin.site.register(RecommendationsBPC)
admin.site.register(RecommendationsKD)
admin.site.register(RecommendationsAccs)
admin.site.register(RecommendationsMF)
admin.site.register(TxnHistory)



