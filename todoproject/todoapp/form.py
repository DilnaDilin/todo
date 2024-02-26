from django import forms
from .models import Task

class todoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']

