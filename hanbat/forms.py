from django import forms
from .models import pyth

class pythform(forms.ModelForm):
    class Meta:
        model = pyth
        fields = '__all__'
       
        # fields = ['title', 'body']

