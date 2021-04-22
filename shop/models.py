from django.db import models
# from . import views
class Product(models.Model):
    # le=views.mode()
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default='')
    subcategory=models.CharField(max_length=50, default='') 
    price=models.IntegerField(default=0)   
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image = models.ImageField(upload_to='shop/images', default="empty")
    def __str__(self):
        return self.product_name
    product_no=models.IntegerField(default=0)