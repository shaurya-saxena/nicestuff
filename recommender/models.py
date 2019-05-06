from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=50, db_column='Name')
    desc = models.CharField(max_length=500, db_column='Description')
    cat = models.CharField(max_length=50, db_column='Category')
    price = models.IntegerField(db_column='Price')
    image_url = models.CharField(max_length=200, db_column='Image Link')
    seller_url = models.CharField(max_length=200, db_column='Seller Link')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"
     
class Recommendations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6', default='1')
    rec7 = models.IntegerField(db_column='Recommendation 7', default='2')
    rec8 = models.IntegerField(db_column='Recommendation 8', default='3')
    rec9 = models.IntegerField(db_column='Recommendation 9', default='4')
   

    class Meta:
        verbose_name_plural = "Recommendations"

        