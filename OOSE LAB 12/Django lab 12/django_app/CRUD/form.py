from django import forms
from .models import Students


class std(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('std_name', 'std_contact','std_roll', 'project')
        labels = {'std_name':'Student Name', 'std_contact':'Student Contact', 'std_roll':'Student Rollno', 'project':'Student Project'}
    
    def __init__(self, *args, **kwargs):
        super(std, self).__init__(*args, **kwargs)
        self.fields['project'].empty_label = "Select"
        
