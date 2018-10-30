from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import views, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import LoginForm

class LoginView(views.LoginView):
  template_name = 'user/login.html'


def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      user = form.save()
      login(request, user)
      return render(request, 'user/signup_completion.html')
    else:
      return render(request, 'user/signup.html', { 'form': form })
  else:
    form = UserCreationForm()
    return render(request, 'user/signup.html', { 'form': form })


def profile(request, username):
  user = User.objects.get(username=username)
  return render(request, 'user/profile.html', { 'user': user })