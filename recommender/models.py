from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=50, db_column='Name')
    desc = models.Charfield(max_length=500, db_column='Description')
    cat = models.Charfield(max_length=50, db_column='Category')
    price = models.IntegerField(db_column='Price')
    image_url = models.Charfield(max_length=200, db_column='Image Link')
    seller_url = models.Charfield(max_length=200, db_column='Seller Link')
     