from django import forms 
from .models import *

class CriminalForm(forms.ModelForm): 

    def get_img(img):
        return img

    class Meta: 
        model = criminal
        fields = ['criminal_name','criminal_Img'] 