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
                'placeholder': '내용',
                'class': 'form-control',
            }),
            'duedate': forms.SelectDateWidget(attrs={
                'placeholder': '마감기한',
                'class': 'form-control',
            }),
            'priority': forms.Select(attrs={
                'placeholder': '우선 순위',
                'class': 'form-control',
            })
        }