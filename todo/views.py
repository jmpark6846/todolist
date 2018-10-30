from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.filter(author=request.user)
    context = { 'todos': todos }
    return render(request, 'todo/todo_list.html', context)










@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.create(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                author = request.user,
                duedate = form.cleaned_data['duedate']
            )
            return redirect(reverse('todo:list'))
        else:
            context = { 'form': form }
            return render(request, 'todo/todo_create.html', context)
    else:
        form = TodoForm()
        context = { 'form': form }
        return render(request, 'todo/todo_create.html', context)


