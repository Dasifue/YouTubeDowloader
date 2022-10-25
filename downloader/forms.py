from django import forms
from django import forms

class VideoURLForm(forms.Form):
    
    url = forms.URLField()

