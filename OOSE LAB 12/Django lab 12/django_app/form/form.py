from django import forms
from .models import Player, Score

class playerform(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('Name', 'team')
