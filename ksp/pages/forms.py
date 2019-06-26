from django import forms 
from .models import *

class CriminalForm(forms.ModelForm): 
  
    class Meta: 
        model = criminal
        fields = ['criminal_name','criminal_Img'] 