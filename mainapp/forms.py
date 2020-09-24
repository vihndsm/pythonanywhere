from django import forms 
from .models import Applications

class ApplicationsForm(forms.ModelForm):
  class Meta:
        model = Applications
        fields = ['name', 'mail', 'comment']
