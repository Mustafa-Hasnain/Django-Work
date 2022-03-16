from django import forms
from .models import Customer,Account

class cus(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name', 'gender','customer_address', 'customer_contact', 'customer_DOB')
        labels = {
            'customer_name' : 'Name',
            'gender': 'Gender',
            'customer_address' : 'Address',
            'customer_contact' : 'Contact',
            'customer_DOB' : 'DOB'
        }

    def __init__(self, *args, **kwargs):
        super(cus, self).__init__(*args, **kwargs)

class acc(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('account_num', 'account_name','balance', 'branch_name','customer_name')
        labels = {
            'account_num' : 'Account Number',
            'account_name': 'Account Name',
            'balance' : 'Balance',
            'branch_name' : 'Branch Name'
        }

    def __init__(self, *args, **kwargs):
        super(acc, self).__init__(*args, **kwargs)
        self.fields['customer_name'].empty_label = "Select"

class Withdraw(forms.Form):
    acc_no = forms.CharField()
    amount = forms.IntegerField()

class Transfer(forms.Form):
    acc_no1 = forms.CharField(required=False)
    acc_no2 = forms.CharField()
    amount = forms.IntegerField()

