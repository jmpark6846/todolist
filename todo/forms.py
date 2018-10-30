from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'duedate']
        widgets = {
            'title': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': '제목',
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'duedate': forms.DateTimeInput(attrs={
                'class': 'form-control',
            })
        }