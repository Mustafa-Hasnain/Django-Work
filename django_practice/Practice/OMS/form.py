import django
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.forms.utils import ValidationError

from OMS.models import Customer, Product, Order, Bill

class sign_up(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ['customer_name', 'customer_email', 'customer_password', 
         'customer_address']
         
         
    def confirm_password(self):
        cleaned_data = super(sign_up, self).clean()
        pass1 = cleaned_data.get('customer_password')
        pass2 = cleaned_data.get('confirm_password')

        if pass1 != pass2:
            raise forms.ValidationError("Passwords Doesnt Match!!!")

class addproduct(forms.ModelForm):
    class Meta:
        model=Product
        fields = ['product_name','customer']
        labels = {'product_name':'Customer_Name', 'customer':'Room No'}
