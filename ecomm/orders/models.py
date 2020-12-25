from django.db import models
from products.models import Product
from customers.models import Customer
import datetime
# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    mob_no = models.CharField(max_length=50,default='',blank=True)
    datetime = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)