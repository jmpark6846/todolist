from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required()
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    data = { 'todo' : todo }
    return render(request, 'todo/todo_detail.html', data)


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Todo
    form_class = TodoForm
    context_object_name = 'todo'
    template_name = 'todo/todo_update.html'

    def get_success_url(self):
        return reverse('todo:detail', kwargs={'pk': self.object.pk})


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')

