from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'content', 'duedate', 'priority', 'done']
        widgets = {
            'title': forms.TextInput(attrs={
                'autocomplete': 'off',
                'placeholder': '제목',
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': '내용',
                'class': 'form-control',
            }),
            'duedate': forms.DateInput(attrs={
                'placeholder': '마감기한(선택)',
                'autocomplete': 'off',
                'class': 'form-control',
            }),
            'priority': forms.Select(attrs={
                'placeholder': '우선 순위',
                'class': 'form-control',
            })
        }