from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TodoForm
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.filter(author=request.user)
    # 마감 기한이 지난 할일들 고르기
    expired = todos.filter(done=False, duedate__lt=timezone.now())

    context = { 'todos': todos, 'expired':expired }
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
            return render(request, 'todo/todo_form.html', context)
    else:
        form = TodoForm()
        context = { 'form': form }
        return render(request, 'todo/todo_form.html', context)


@login_required
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk, author=request.user)
    data = { 'todo' : todo }
    return render(request, 'todo/todo_detail.html', data)


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Todo
    form_class = TodoForm
    context_object_name = 'todo'
    template_name = 'todo/todo_form.html'

    def get_queryset(self):
        queryset = super(TodoUpdateView, self).get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('todo:detail', kwargs={'pk': self.object.pk})


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')

    def get_queryset(self):
        queryset = super(TodoDeleteView, self).get_queryset()
        return queryset.filter(author=self.request.user)


@login_required
def todo_toggle_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk, author=request.user)
    todo.done = not todo.done
    todo.save()
    context = {
        'todo': todo.id,
        'done': todo.done
    }
    return JsonResponse(context)
