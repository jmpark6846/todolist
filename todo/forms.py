from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'content', 'duedate', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': '제목',
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'duedate': forms.Select(attrs={
                'class': 'form-control',
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
            })
        }