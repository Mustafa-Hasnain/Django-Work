from django.db import models

# Create your models here.
from django.db import models

class Customer (models.Model):
    customer_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    customer_address = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=50)
    customer_DOB = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name

class Account (models.Model):
    account_num = models.CharField(max_length=50)
    account_name= models.CharField(max_length=50)
    balance=models.IntegerField()
    branch_name= models.CharField(max_length=50)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_num

