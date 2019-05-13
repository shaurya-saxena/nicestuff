from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    pid = models.IntegerField(primary_key=True, db_column='Product ID')
    name = models.CharField(max_length=50, db_column='Name')
    desc = models.CharField(max_length=500, db_column='Description')
    cat = models.CharField(max_length=50, db_column='Category')
    price = models.IntegerField(db_column='Price')
    image_url = models.CharField(max_length=200, db_column='Image Link')
    seller_url = models.CharField(max_length=200, db_column='Seller Link')

    def __str__(self):
        return self.pid

    class Meta:
        verbose_name_plural = "Products"
     

class RecommendationsMA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsWA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsTech(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsHD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsFurn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsWF(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsBPC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsKD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsAccs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
class RecommendationsMF(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='User')
    rec1 = models.IntegerField(db_column='Recommendation 1')
    rec2 = models.IntegerField(db_column='Recommendation 2')
    rec3 = models.IntegerField(db_column='Recommendation 3')
    rec4 = models.IntegerField(db_column='Recommendation 4')
    rec5 = models.IntegerField(db_column='Recommendation 5')
    rec6 = models.IntegerField(db_column='Recommendation 6')
    rec7 = models.IntegerField(db_column='Recommendation 7')
    rec8 = models.IntegerField(db_column='Recommendation 8')
    rec9 = models.IntegerField(db_column='Recommendation 9')
   

class TxnHistory(models.Model):
    txnid = models.IntegerField(db_column='Transaction ID', primary_key=True)
    pid = models.IntegerField(db_column='Product ID')
    user = models.IntegerField(db_column='User ID')
    status = models.BooleanField(db_column='Status')
    timestamp = models.IntegerField(db_column='Timestamp in seconds since 1 January 2019')
  


