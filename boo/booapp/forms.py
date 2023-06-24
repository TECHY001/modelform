from .models import don
from django import forms

class Createuser(forms.ModelForm):
    
    class Meta:
        model=don
        fields=['name','contact']
        widgets={
            'name':forms.TextInput(), 
            'contact':forms.TextInput()
        }    