from django.utils import timezone
from django.core.exceptions import FieldError
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TodoForm
from .models import Todo

@login_required
def todo_list(request):
    sort_by = request.GET.get('sort_by')

    if not sort_by:
        if 'sort_by' in request.session:
            sort_by = request.session['sort_by']
        else:
            sort_by = '-created'
            request.session['sort_by']=sort_by
    else:
        request.session['sort_by'] = sort_by

    try:
        todos = Todo.objects.filter(author=request.user).order_by(sort_by)
        expired = todos.filter(done=False, duedate__lt=timezone.now())
        done = todos.filter(done=True)
        alive = todos.filter(done=False)
        context = {'done': done, 'alive': alive, 'expired': expired}

        return render(request, 'todo/todo_list.html', context)
    except FieldError:
        return HttpResponseNotFound()


def url_with_querystring(path, **kwargs):
    import urllib
    return path + '?' + urllib.parse.urlencode(kwargs)


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo(**form.cleaned_data)
            todo.author = request.user
            todo.save()
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
        return reverse('todo:list')


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
