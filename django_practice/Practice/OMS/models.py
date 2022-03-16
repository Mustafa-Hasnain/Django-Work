from django.db import models
# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_dob = models.DateField(auto_now=True)
    customer_email = models.EmailField(default='non@gmail.com')
    customer_password = models.CharField(max_length=10)
    customer_address = models.TextField()

class Product(models.Model):
    product_no = models.CharField(default='P-###', max_length=50)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

class Order(models.Model):
    order_no = models.CharField(default='O-###',max_length=50)
    order_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    delivery_address = models.CharField(max_length=200)
    product = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer = models.ForeignKey(Product, on_delete=models.CASCADE)

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


 