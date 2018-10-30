from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.filter(author=request.user)
    context = { 'todos': todos }
    return render(request, 'todo/list.html', context)
