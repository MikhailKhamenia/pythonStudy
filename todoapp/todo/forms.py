from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('title')
        if data:
            cleaned_data['title'] = data.replace('c','$')
        return cleaned_data