from django.shortcuts import render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.filter(author=request.user)
    context = { 'todos': todos }
    return render(request, 'todo/list.html', context)

