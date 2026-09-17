from .models import *
from django.forms import ModelForm, TextInput, Select, Textarea, ClearableFileInput


class Create(ModelForm):
    class Meta:
        model = Request
        fields = ['Customers_full_name', 'Lecture_hall', 'Description', 'Work', 'Performer', 'Comment', 'Files',
                  'Condition']
        widgets = {
            'Customers_full_name': TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'Lecture_hall': TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'Description': Textarea(attrs={'class': 'form-control', 'style': 'width: 500px; resize: none;',
                                           'cols': '50', 'rows': '3'}),
            'Work': Select(attrs={'class': 'form-select', 'style': 'width: 500px;'}),
            'Performer': Select(attrs={'class': 'form-select', 'style': 'width: 500px;'}),
            'Comment': Textarea(attrs={'class': 'form-control', 'style': 'width: 500px; resize: none;', 'cols': '50',
                                       'rows': '3'}),
            'Files': ClearableFileInput(attrs={'type': 'file', 'class': 'form-control', 'style': 'width: 500px;'}),
            'Condition': Select(attrs={'class': 'form-select', 'style': 'width: 500px;'}),
        }