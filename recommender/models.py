from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    cat = models.CharField(max_length=50)
    price = models.IntegerField()
    image_url = models.CharField(max_length=200)
    seller_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"
        db_table = 'Products'
     

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
    
    class Meta:
        verbose_name_plural = "Men's Apparel Recommendations"
        verbose_name = "Men's Apparel Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Women's Apparel Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Tech Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Home Decor Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Furniture Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Women's Footwear Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Beauty and Personal Care Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Kitchen and Dining Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Accessories Recommendations"
    
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

    class Meta:
        verbose_name_plural = "Men's Footwear Recommendations"
    
class TxnHistory(models.Model):
    txnid = models.IntegerField(primary_key=True)
    pid = models.IntegerField()
    user = models.IntegerField()
    status = models.BooleanField()
    timestamp = models.IntegerField()

    class Meta:
        verbose_name_plural = "Transaction History"
    


