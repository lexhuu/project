from django import forms
from .models import *

class empform(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'