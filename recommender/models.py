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



class Recommendations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE) 
    score = models.FloatField()
    rank = models.IntegerField()

    def __str__(self):
        return "Recommendation " + str(self.rank) + " for " + str(self.user) 

    class Meta:
        verbose_name_plural = "Recommendations"
        verbose_name = "Recommendations"
        db_table = "Recommendations"
        unique_together = (('user', 'rank'))




class TxnHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)
    status = models.BooleanField()
    timestamp = models.IntegerField()

    def __str__(self):
        return str(self.user) + " liking status for " + str(self.pid) 

    class Meta:
        verbose_name_plural = "Transaction History"
        db_table = "TxnHistory"
        unique_together = (('user', 'pid'))




